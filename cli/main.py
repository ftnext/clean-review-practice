from reviewlogic.drivers import proposal_driver
from reviewlogic.gateways import proposal_gateway
from reviewlogic.usecases import proposal_usecase
from reviewlogic.value_objects import ProposalId

if __name__ == "__main__":
    driver = proposal_driver.InMemoryProposalDriver()
    port = proposal_gateway.ProposalGateway(driver)
    usecase = proposal_usecase.ProposalUseCase(port)

    input("Welcome to the review app [Press Enter]")
    print("")

    proposals = usecase.list()
    print("Proposals\n")
    for p in proposals:
        print(f"- {p.id} {p.title}")
    print("")

    while True:
        entered = input(
            "Select id to review target [ex. 108] (Exit [Press q]): "
        )
        stripped = entered.strip()
        if not stripped:
            continue
        if stripped.lower() == "q":
            break

        try:
            entered_id = int(stripped)
        except ValueError:
            print("Error: Please input as an integer")
            continue

        proposal_id = ProposalId(entered_id)
        try:
            proposal = usecase.find_by(proposal_id)
        except ValueError as ex:
            print(f"Error: {ex}")
            continue

        print(f"{proposal.title} (Id={proposal.id})")
        print("")
        print(proposal.description)
        print("")
