def generate_hashtags(keywords):
    # Split keywords and create hashtags
    keyword_list = keywords.lower().replace(",", "").split()
    hashtags = [f"#{keyword}" for keyword in keyword_list]
    
    # Add some generic hashtags based on keywords
    generic_hashtags = ["#SocialMedia", "#Marketing", "#Branding"]
    hashtags.extend(generic_hashtags[:2])  # Limit to 2 generic hashtags

    return " ".join(hashtags)