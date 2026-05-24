def get_response(user_input):

    user_input = user_input.lower()

    # Greetings
    if user_input in ["hello", "hi", "hey"]:
        return "Hello CEO! How can I help your startup today?"

    # Hiring
    elif "hire developer" in user_input:
        return "Hiring a skilled developer can improve product quality and speed."

    elif "hire designer" in user_input:
        return "A creative designer can improve your user experience and branding."

    elif "hire marketing team" in user_input:
        return "Marketing teams help increase customer reach and brand awareness."

    # Funding
    elif "funding" in user_input:
        return "You can seek funding through investors, venture capital or crowdfunding."

    elif "investor" in user_input:
        return "Investors usually look for growth potential and strong business ideas."

    # Product Launch
    elif "launch product" in user_input:
        return "Before launching, ensure your product solves a real customer problem."

    elif "new feature" in user_input:
        return "Adding innovative features can attract more users."

    # Marketing
    elif "marketing" in user_input:
        return "Digital marketing and social media campaigns are effective startup strategies."

    elif "social media" in user_input:
        return "Social media can help your startup grow rapidly with low cost."

    # Employees
    elif "employee motivation" in user_input:
        return "Employee motivation improves productivity and workplace culture."

    elif "layoffs" in user_input:
        return "Layoffs should be handled carefully to protect company morale and reputation."

    # Startup Advice
    elif "startup idea" in user_input:
        return "The best startup ideas solve real-world problems."

    elif "growth" in user_input:
        return "Consistent product improvement and customer satisfaction drive growth."

    elif "competition" in user_input:
        return "Study your competitors and focus on what makes your startup unique."

    # Status
    elif "status" in user_input:
        return """
Startup Status:
• Product Development: Active
• Team Performance: Stable
• Marketing: Running
• Investor Interest: Moderate
"""

    # Help
    elif "help" in user_input:
        return """
You can ask me about:
• Hiring
• Marketing
• Funding
• Product Launch
• Startup Growth
• Investors
"""

    # Exit
    elif user_input in ["bye", "exit", "quit"]:
        return "Goodbye CEO! Wishing success to your startup!"

    # Default
    else:
        return "Sorry CEO, I don't understand that startup command."