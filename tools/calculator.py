def calculator(expression: str):
    """
    Simple calculator tool that evaluates math expressions.
    Example: '25 * 14'
    """

    try:
        result = eval(expression)
        return str(result)
    except Exception as e:
        return f"Error calculating expression: {str(e)}"