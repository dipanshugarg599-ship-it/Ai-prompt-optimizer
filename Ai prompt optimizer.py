print("=" * 60)
print("       🤖 AI PROMPT OPTIMIZER BOT")
print("=" * 60)

def optimize_prompt(question):

    q = question.lower()

    if "python" in q or "program" in q or "code" in q:
        role = "Senior Python Developer"

    elif "machine learning" in q or "ai" in q:
        role = "AI and Machine Learning Expert"

    elif "cricket" in q or "match" in q or "sports" in q:
        role = "Professional Sports Analyst"

    elif "fitness" in q or "exercise" in q or "workout" in q:
        role = "Certified Fitness Coach"

    elif "study" in q or "exam" in q or "assignment" in q:
        role = "Experienced Academic Tutor"

    elif "story" in q or "poem" in q or "write" in q:
        role = "Professional Creative Writer"

    else:
        role = "Subject Matter Expert"

    prompt = f"""
You are a {role}.

USER REQUEST:
{question}

TASK:
Understand the user's request and provide the best possible answer.

INSTRUCTIONS:
1. Explain clearly.
2. Give the answer step-by-step.
3. Use simple language.
4. Give examples where useful.
5. Avoid unnecessary information.

OUTPUT:
Give a clear, accurate and well-structured answer.
"""

    return role, prompt


while True:

    question = input("\nEnter your question (or type exit): ")

    if question.lower() == "exit":
        print("\n🤖 Bot closed successfully!")
        break

    if question.strip() == "":
        print("⚠️ Please enter a question.")
        continue

    role, prompt = optimize_prompt(question)

    print("\n" + "=" * 60)
    print("✨ OPTIMIZED PROMPT")
    print("=" * 60)

    print(prompt)

    print("🎯 Detected Role:", role)
    print("=" * 60)