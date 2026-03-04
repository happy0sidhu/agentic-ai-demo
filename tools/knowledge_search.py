knowledge_base = {
    "docker": "Docker containers package applications with all dependencies so they run consistently across environments.",
    
    "kubernetes": "Kubernetes is a container orchestration platform that manages deployment, scaling, and operation of containerized applications.",
    
    "autoscaling": "Autoscaling automatically adjusts the number of running instances of an application based on traffic or resource usage.",
    
    "api": "An API (Application Programming Interface) allows software systems to communicate with each other."
}


def search_knowledge(query: str):
    """
    Searches a small internal knowledge base.
    """

    query = query.lower()

    for key in knowledge_base:
        if key in query:
            return knowledge_base[key]

    return "No relevant information found in knowledge base."