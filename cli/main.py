from reviewlogic.drivers import proposal_driver
from reviewlogic.gateways import proposal_gateway
from reviewlogic.usecases import proposal_usecase


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
    
    input("Select id to review target [ex. 108]: ")
