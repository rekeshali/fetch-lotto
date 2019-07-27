# code by rborden4
# code to display the data using matplotlib
import matplotlib
import matplotlib.pyplot as plt

# the x range for the mega millions plot
mm_range = range(1, 75)

# plotting the mega millions data
# plot the range of mega millions numbers and frequency with solid cyan line
plt.plot(mm_range, mm_frequency, 'c-', label = 'Lotto Numbers')

# the x range for the megaball plot
mb_range = range(1, 55)

# plotting the megaball data
# plot the range of megaball numbers and frequency with solid orange line
plt.plot(mb_range, mb_frequency, '-', color = "orange", label = 'Megaball')

# adding the legend, title, and labels for axes
plt.legend(shadow=True, loc="upper right")
plt.title("Winning Lotto Numbers Frequency")
plt.xlabel("Ball Number")
plt.ylabel("Frequency")



plt.show()
