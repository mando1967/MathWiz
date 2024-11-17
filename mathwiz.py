import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class MathWiz:
    def __init__(self):
        # Initialize OpenAI client
        self.client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

    def solve_problem(self, problem):
        """
        Solve a mathematical problem using OpenAI's GPT model.
        
        Args:
            problem (str): The mathematical problem to solve
            
        Returns:
            str: The solution with explanation
        """
        try:
            # Create the prompt with specific instructions
            prompt = f"""Please solve this mathematical problem step by step:
            Problem: {problem}
            
            Please provide:
            1. The solution
            2. Step-by-step explanation
            3. Any relevant formulas used"""

            # Make the API call
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful math tutor. Provide clear, step-by-step solutions to mathematical problems."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7
            )
            
            # Extract and return the response
            return response.choices[0].message.content

        except Exception as e:
            return f"An error occurred: {str(e)}"

def main():
    # Create a .env file if it doesn't exist
    if not os.path.exists('.env'):
        with open('.env', 'w') as f:
            f.write('OPENAI_API_KEY=your_api_key_here')
        print("Created .env file. Please add your OpenAI API key to it.")
        return

    mathwiz = MathWiz()
    
    print("Welcome to MathWiz! 🧮✨")
    print("I can help you solve mathematical problems. Type 'quit' to exit.")
    
    while True:
        problem = input("\nEnter your math problem: ")
        
        if problem.lower() == 'quit':
            print("Thank you for using MathWiz! Goodbye! 👋")
            break
            
        solution = mathwiz.solve_problem(problem)
        print("\nSolution:")
        print(solution)

if __name__ == "__main__":
    main()
