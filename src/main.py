from .planner import create_research_plan

def main():

    print("AI Research Assistant - Week 11")

    try:
        query = input("Enter research topic: ")
        count = int(input("Number of papers: "))

        plan = create_research_plan(query, count)

        print(plan.model_dump_json(indent=4))

    except (ValueError, RuntimeError) as error:
        print("Error:", error)

if __name__ == "__main__":
    main()

