from alpaca.broker.client import BrokerClient
from alpaca.broker.requests import CreateACHTransferRequest
from alpaca.broker.enums import TransferDirection, TransferTiming

broker_client = BrokerClient('AKJUKL5OYI6SZVE913B0', 'tmf30hOiVRe980o4V6xZO5eVbcUXVtMFFuUVAWKe')
account_id = "c8f1ef5d-edc0-4f23-9ee4-378f19cb92a4"

transfer_data = CreateACHTransferRequest(
                    amount=10,
                    direction=TransferDirection.INCOMING,
                    timing=TransferTiming.IMMEDIATE,
                    relationship_id="0f08c6bc-8e9f-463d-a73f-fd047fdb5e94"
                )
transfer = broker_client.create_transfer_for_account(
                account_id=account_id,
                transfer_data=transfer_data
            )