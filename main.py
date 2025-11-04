from sklearn.linear_model import LinearRegression

print("✨ Welcome to the Simple AI Training Tool! ✨")
print("This program trains a basic AI model using linear regression.")
print("Just enter your data points and get predictions! 🚀")

# Step 1: How many data points do you want to add?
data_counter = int(input("How many data points would you like to enter? "))

# Step 2: Collect X (input) and Y (output) values
input_value = []  # Will store all X values (input)
exit_value = []  # Will store all Y values (output)

for i in range(data_counter):
    print(f"\n--- Step {i+1} ---")
    i_val = float(input(f"Enter input_value value {i+1}: "))
    e_val = float(input(f"Enter exit_value value {i+1}: "))
    input_value.append([i_val])  # Store as 2D array (required by sklearn)
    exit_value.append(e_val)

# Step 3: Train the AI model
print("\n🤖 Training the AI model... (this takes 1 second)")
model = LinearRegression()
model.fit(input_value, exit_value)

# Step 4: Get a prediction
input_value_new = float(input("\nEnter X value to predict: "))
prediction = model.predict([[input_value_new]])  # Predict for the new value

# Step 5: Show result
print(f"\n✅ Prediction: {prediction[0]:.2f}")
print("Your AI model has learned from your data and made this prediction! 💡")
