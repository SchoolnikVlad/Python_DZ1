from address import Address
from mailing import Mailing

to_address = Address("123456", "Moscow", "Main Street", "1", "fl 101")
from_address = Address("654321", "Saint Petersburg", "Second Street", "2", "fl 202")
cost = 100.50
track = "ABC123"

mailing = Mailing(to_address, from_address, cost, track)

print(f"Mailing {mailing.track} from {mailing.from_address.index}, {mailing.from_address.city}, {mailing.from_address.street}, {mailing.from_address.house} - {mailing.from_address.flat} to {mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.street}, {mailing.to_address.house} - {mailing.to_address.flat}. Cost {mailing.cost} rubles.")