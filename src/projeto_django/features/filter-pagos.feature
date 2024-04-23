Feature: Filter payed debts
    Scenario: Return payed debts when a client exists
        Given that a client exists for payed debts
        Given that a payment exists for payed debts
        Given that the payment is associated with the client for payed debts
        Given that the payment was paid
        When I filter the payed debts
        Then the payed debts must be returned