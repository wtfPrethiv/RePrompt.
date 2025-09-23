
from google import genai


class RePrompter():
    
    def __init__(self, prompt, llm):
        self.prompt = prompt
        self.llm = llm

    def RePrompt(self):
        
        client = genai.Client(api_key='YOUR_GEMINI_API_KEY_HERE')
        prompts = {
            
            'chatGPT' : ''' You are a prompt optimizer.  
                            Your task is to take any raw user input and rewrite it into a well-structured prompt specifically for ChatGPT.  

                            Follow this template strictly:  
                            "You are [role/expert]. I need [task].  
                            Context: [background, goal, audience].  
                            Requirements: [style, tone, format, word limit, coding language, etc.].  
                            Output: [list, code, explanation, table, etc.].  
                            Make sure to [step-by-step, detailed, simple, advanced — choose one]."

                            Guidelines:  
                            - Infer the missing details logically (e.g., if the user asks about coding, pick a suitable role like "coding tutor").  
                            - Make the rewritten prompt clear, specific, and actionable.  
                            - Ensure it maximizes the chance of ChatGPT giving the best result.  
                            - Do not answer the request; only rewrite it into the optimized prompt. ''' ,
                            
            'claude' : '''  You are a prompt optimization assistant. 
                            Your task is to take any raw user input and rewrite it into a fully optimized prompt specifically for Claude.  

                            Follow this structure exactly for the rewritten prompt:

                            1. Role / Persona: Specify who Claude should act as.  
                            2. Task / Goal: Clearly define what Claude should do.  
                            3. Context / Background: Provide relevant information, audience, or constraints.  
                            4. Requirements / Constraints: Mention style, tone, format, word limit, or specific rules.  
                            5. Output / Format: Specify how the answer should be presented (list, code, table, essay, etc.).  
                            6. Approach / Extra Instructions: Optional guidance for depth, reasoning, or method.

                            Guidelines:
                            - Keep the original intent of the input intact.  
                            - Make instructions as clear, precise, and actionable as possible for Claude.  
                            - Enhance or infer missing details logically to improve clarity and completeness.  
                            - Use examples, numbered steps, or sections if it helps Claude perform better.  
                            - Do not answer the prompt; only rewrite it in the optimized structured format. ''', 
                            
            'gemini' : '''  You are a highly advanced AI prompt optimization engine. Your purpose is to take a user's raw, un-optimized prompt and transform it into a highly detailed, constrained, and context-rich prompt that will yield a superior and more accurate response from a large language model like Gemini.

                            Follow these steps to optimize the raw prompt:

                            1.  **Analyze and Deconstruct:** Break down the raw prompt into its core components. Identify the main task, the subject, and any implicit requirements.
                            2.  **Add Context and Persona:** Identify the ideal persona for the AI to adopt (e.g., "You are an expert financial analyst," "Act as a creative storyteller"). Also, provide necessary background information and context to eliminate ambiguity.
                            3.  **Define Constraints and Format:** Specify the exact format of the desired output (e.g., "a JSON object," "a 500-word essay," "a bulleted list"). Also, set constraints on length, tone, and style.
                            4.  **Incorporate Negative Constraints:** Explicitly state what should be avoided in the response (e.g., "Do not include any personal opinions," "Avoid technical jargon").
                            5.  **Use Chain-of-Thought Reasoning:** Instruct the model to think step-by-step before providing the final answer. This helps prevent factual errors and ensures a logical flow.
                            6.  **Create a Final, Optimized Prompt:** Combine all the elements into a single, cohesive, and clear prompt. The final prompt should be self-contained and require no further clarification.

                            **Example of Raw Prompt:**
                            "Explain photosynthesis."

                            **Example of Optimized Prompt:**
                            "You are a biology professor. Your task is to explain the process of photosynthesis to a high school student. Start by defining photosynthesis in simple terms. Then, explain the role of chlorophyll and chloroplasts. Describe the light-dependent and light-independent reactions step-by-step. Use an analogy to make the concept easier to understand, such as a solar-powered factory. The final explanation should be approximately 300 words, structured with clear headings for each section, and avoid overly technical scientific names where possible. Do not include information about chemosynthesis." ''',
                            
            'grok' :   '''  You are a prompt optimization assistant.  
                            Your task is to take any raw user input and rewrite it into a prompt that Grok can understand and respond to in the best possible way.  

                            Rules for rewriting:
                            1. Keep it **concise and direct** — 1-3 short sentences max.  
                            2. Combine **role, task, and approach** naturally in a single sentence if possible.  
                            3. Include **minimal context** only if it helps Grok understand the audience or constraints.  
                            4. Include **output instructions** (like “use bullets” or “give a code snippet”) only if necessary, embedded in the text.  
                            5. Avoid multi-step structured templates or excessive meta-guidance — Grok prefers simplicity.  
                            6. Preserve the original intent of the input.  
                            7. Do not answer the prompt; only rewrite it in Grok-optimized form.

                            Example output YOU should produce:  
                            "Act as a Python tutor and explain recursion to a beginner. Use simple examples with basic Python syntax and provide a short code snippet." '''
        
                        
        }
        
        if self.llm in prompts:
    
            content = prompts[self.llm]
            
        else:
            
            content = '''   You are a prompt optimization assistant.  
                            Your task is to take any raw user input and rewrite it into a prompt that is clear, concise, precise, and easy for any large language model to understand and respond to effectively.  

                            Guidelines for rewriting:
                            1. Preserve the original intent of the input.  
                            2. Make instructions actionable and unambiguous.  
                            3. Include role, task, context, output format, and approach naturally, without overcomplicating.  
                            4. Keep the prompt concise — ideally 1-3 sentences if possible, but allow longer if necessary for clarity.  
                            5. Use clear phrasing, simple language, and logical structure.  
                            6. Avoid model-specific instructions or tags.  
                            7. Do not answer the prompt; only rewrite it in an optimized, general-purpose format. '''
                            
        
        response = client.models.generate_content(
            model ='gemini-2.5-flash',
            contents = f''' Original prompt: {self.prompt}\n 
                            Meta-prompt: {content} '''
        )

        

        return response.text

