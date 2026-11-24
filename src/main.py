
from .planner import create_research_plan
from .paper_search import search_papers


def main():

    print("=" * 60)
    print("AI RESEARCH ASSISTANT")
    print("Week 12 - Core Functionality")
    print("=" * 60)

    try:

        query = input("Enter research topic: ")
        count = int(input("Number of papers: "))

        print("\nCreating research plan...")

        plan = create_research_plan(
            query,
            count
        )

        print("\nRESEARCH PLAN:")
        print(plan.model_dump_json(indent=4))

        print("\nSearching scientific papers...")

        papers = search_papers(
            query=plan.search_queries[0],
            max_results=count
        )

        if not papers:

            print("No relevant papers found.")
            return

        print("\nPapers found:", len(papers))

        for i, paper in enumerate(papers, 1):

            print("\n" + "-" * 60)

            print(f"Paper {i}")
            print("Title:", paper.title)
            print("Authors:", ", ".join(paper.authors))
            print("Year:", paper.publication_year)
            print("DOI:", paper.doi)
            print("Citations:", paper.cited_by_count)
            print("URL:", paper.url)
            print("Abstract:", paper.abstract or "Unavailable")

        if len(papers) < count:

            print(
                "\nWarning: fewer papers found "
                "than requested."
            )

    except (ValueError, RuntimeError) as error:

        print("Error:", error)


if __name__ == "__main__":
    main()


