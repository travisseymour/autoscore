import ast
import operator

# Allowed operations
OPS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.UAdd: operator.pos,
    ast.USub: operator.neg,
}


def safe_eval_math(expression: str) -> float:
    """Safely evaluate a math expression with +, -, *, /, and parentheses."""

    def _evaluate(node):
        if isinstance(node, ast.Expression):  # Root node
            return _evaluate(node.body)
        elif isinstance(node, ast.BinOp):  # Binary operations (+, -, *, /)
            left = _evaluate(node.left)
            right = _evaluate(node.right)
            return OPS[type(node.op)](left, right)
        elif isinstance(node, ast.UnaryOp):  # Unary operations (+, -)
            operand = _evaluate(node.operand)
            return OPS[type(node.op)](operand)
        elif isinstance(node, ast.Num):  # Numbers (int or float)
            return node.n
        elif isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):  # Python 3.8+
            return node.value
        else:
            raise ValueError("Invalid expression")

    try:
        tree = ast.parse(expression, mode="eval")  # Parse into AST
        return _evaluate(tree.body)
    except (SyntaxError, ValueError, KeyError):
        raise ValueError("Invalid mathematical expression")


if __name__ == "__main__":
    # Example Usage:
    print(safe_eval_math("3 + 5 * (2 - 8)"))  # -25.0
    print(safe_eval_math("-4 / 2"))  # -2.0
    print(safe_eval_math("3.5 + 2.5"))  # 6.0
