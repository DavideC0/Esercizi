def isPalidrome(input: int) -> bool:
    sinput = str(input)
    if sinput == sinput[::-1]:
        return True
    else:
        return False

print(isPalidrome(121))
print(isPalidrome(123))