from reviewlogic.domains import proposal as p
from reviewlogic.domains import review as r
from reviewlogic.drivers import proposal_driver as pd
from reviewlogic.drivers import review_driver as rd
from reviewlogic.gateways import proposal_gateway as pg
from reviewlogic.gateways import review_gateway as rg
from reviewlogic.usecases import proposal_usecase as pu
from reviewlogic.usecases import review_usecase as ru
from reviewlogic.value_objects import ProposalId, UserId


def configure_proposal_logic() -> pu.ProposalUseCase:
    proposal_driver = pd.InMemoryProposalDriver()
    proposal_port = pg.ProposalGateway(proposal_driver)
    return pu.ProposalUseCase(proposal_port)


def configure_review_logic() -> ru.ReviewUseCase:
    review_driver = rd.InMemoryReviewDriver()
    review_port = rg.ReviewGateway(review_driver)
    return ru.ReviewUseCase(review_port)


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


def enter_review_score() -> r.ScoreEnum:
    while True:
        entered = input("Input score [Yes / Maybe / No]: ")
        try:
            score = r.ScoreEnum(entered.strip().title())
        except ValueError:
            print(f"Error: {entered} is not valid as score")
            continue
        return score


if __name__ == "__main__":
    proposal_usecase = configure_proposal_logic()
    review_usecase = configure_review_logic()

    input("Welcome to the review app [Press Enter]")
    print("")

    # Dummy login
    USER_ID = UserId(101)

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

        entered = input("Review this proposal? [y/N] ")
        if entered.strip().lower() != "y":
            continue

        score = enter_review_score()
        comment = input("Input comment: ")

        review_usecase.save(USER_ID, proposal_id, score, comment)
