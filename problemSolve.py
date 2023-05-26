import openai

openai.api_key = ''

def solveProblem(problem):
    message = prompt = f"""
    Given the following problem:

    {problem}

    Write a Python function to solve it.
    """

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=0.5,
        max_tokens=100

    )
    return response.choices[0].text.strip()
problem = "ecrit une fonction qui renvoie la somme de deux entiers"
solution = solveProblem(problem)
print(solution)
