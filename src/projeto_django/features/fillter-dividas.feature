Feature: Filter Dividas

    Scenario: Return a debt when a client exists
        Given that a client exists for debts
        Given that a payment exists for debts
        Given that the payment is associated with the client for debts
        Given that the payment was not paid
        When I filter the debts
        Then the debt must be returned
