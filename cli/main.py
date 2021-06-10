from reviewlogic.domains import proposal as p
from reviewlogic.drivers import proposal_driver as pd
from reviewlogic.gateways import proposal_gateway as pg
from reviewlogic.usecases import proposal_usecase as pu
from reviewlogic.value_objects import ProposalId


def configure_proposal_logic() -> pu.ProposalUseCase:
    proposal_driver = pd.InMemoryProposalDriver()
    proposal_port = pg.ProposalGateway(proposal_driver)
    return pu.ProposalUseCase(proposal_port)


def show_proposals_list(proposals: p.Proposals) -> None:
    print("Proposals\n")
    for p in proposals:
        print(f"- {p.id} {p.title}")
    print("")


def show_proposal_detail(proposal: p.Proposal) -> None:
    print(f"{proposal.title} (Id={proposal.id})")
    print("")
    print(proposal.description)
    print("")


if __name__ == "__main__":
    proposal_usecase = configure_proposal_logic()

    input("Welcome to the review app [Press Enter]")
    print("")

    proposals = proposal_usecase.list()
    show_proposals_list(proposals)

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
            proposal = proposal_usecase.find_by(proposal_id)
        except ValueError as ex:
            print(f"Error: {ex}")
            continue

        show_proposal_detail(proposal)
