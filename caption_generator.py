from transformers import pipeline

def generate_caption(keywords, tone, platform):
    # Initialize text generation pipeline (using a small model for speed)
    generator = pipeline("text-generation", model="distilgpt2")

    # Create prompt based on inputs
    prompt = f"Write a {tone} social media caption for {platform} about {keywords}."
    max_length = 60 if platform == "Twitter" else 100  # Shorter for Twitter

    # Generate caption
    result = generator(prompt, max_length=max_length, num_return_sequences=1)
    caption = result[0]["generated_text"].replace(prompt, "").strip()

    return caption