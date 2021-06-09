from reviewlogic.value_objects.positive_integer_id import PositiveIntegerId


class ProposalId(PositiveIntegerId):
    def __str__(self):
        return str(self.value)
