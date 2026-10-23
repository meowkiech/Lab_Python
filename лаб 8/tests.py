import unittest
from models import TicketStatus
from factories import TicketFactory
from strategies import StandardPricing, DiscountPricing, DynamicPricing
from repositories import InMemoryTicketRepository
from services import TicketService, TicketNotFoundError
from commands import BuyTicketCommand, ReturnTicketCommand


class TicketTests(unittest.TestCase):

    def test_factory_price(self):
        ticket = TicketFactory.create(1, "Иванов И.И.", "001А", "купе")
        self.assertEqual(ticket.base_price, 2500)

    def test_factory_unknown_type(self):
        with self.assertRaises(ValueError):
            TicketFactory.create(1, "Иванов И.И.", "001А", "люкс")

    def test_standard_strategy(self):
        self.assertEqual(StandardPricing().calculate(1000), 1000)

    def test_discount_strategy(self):
        self.assertEqual(DiscountPricing().calculate(1000), 500)

    def test_dynamic_strategy(self):
        self.assertAlmostEqual(DynamicPricing(0.3).calculate(1000), 1300)

    def test_service_create_and_pay(self):
        service = TicketService(InMemoryTicketRepository())
        ticket = service.create_ticket("Иванов И.И.", "001А", "сидячий", StandardPricing())
        service.pay(ticket.id)
        self.assertEqual(ticket.status, TicketStatus.PAID)

    def test_refund_missing(self):
        service = TicketService(InMemoryTicketRepository())
        with self.assertRaises(TicketNotFoundError):
            service.refund(999)

    def test_buy_command(self):
        service = TicketService(InMemoryTicketRepository())
        command = BuyTicketCommand(service, "Петров П.П.", "055В", "СВ", DiscountPricing())
        command.execute()
        self.assertEqual(command.ticket.price, 2500)
        self.assertEqual(command.ticket.status, TicketStatus.PAID)

    def test_return_command(self):
        service = TicketService(InMemoryTicketRepository())
        buy = BuyTicketCommand(service, "Сидоров С.С.", "001А", "купе", StandardPricing())
        buy.execute()
        ReturnTicketCommand(service, buy.ticket.id).execute()
        self.assertEqual(buy.ticket.status, TicketStatus.RETURNED)


if __name__ == "__main__":
    unittest.main()
