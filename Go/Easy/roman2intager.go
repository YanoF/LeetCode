func romanToInt(s string) int {
    values := map[byte]int{
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000,
    }

    total := 0
    for i := 0; i < len(s); i++ {
        value := values[s[i]]
        if i+1 < len(s) && value < values[s[i+1]] {
            total -= value
        } else {
            total += value
        }
    }
    return total
}