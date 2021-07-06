# Ask the user if they have played before.
played_before = input("Have you played this game before?")

# If they say "yes", output "program continues".
if played_before == "yes" or "y" or "yEs" or "Yes" or "YES":
    print("Output continues.")
elif played_before == "no" or "n" or "No" or "NO" or "nO":
    print("Display instructions.")
# If they say "no", output "display instructions".

