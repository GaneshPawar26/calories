# import pandas as pd
# import plotly.graph_objects as go

# # Load the data from CSV file
# data = pd.read_csv("calories_data.csv")

# # Convert the date column to datetime format
# data['Date'] = pd.to_datetime(data['Date'])

# # Plot 1: Calories Consumed Over Time
# fig1 = go.Figure()
# fig1.add_trace(go.Scatter(x=data['Date'], y=data['Calories'], mode='lines', name='Calories'))
# fig1.update_layout(title='Calories Consumed Over Time', xaxis_title='Date', yaxis_title='Calories')

# # Plot 2: Exercise vs Calories
# fig2 = go.Figure()
# fig2.add_trace(go.Scatter(x=data['Exercise'], y=data['Calories'], mode='markers', name='Exercise vs Calories'))
# fig2.update_layout(title='Exercise vs Calories', xaxis_title='Exercise (minutes)', yaxis_title='Calories')

# # Plot 3: Water Intake Over Time
# fig3 = go.Figure()
# fig3.add_trace(go.Bar(x=data['Date'], y=data['Water Intake'], name='Water Intake'))
# fig3.update_layout(title='Water Intake Over Time', xaxis_title='Date', yaxis_title='Water Intake (ml)')

# # Display the plots
# fig1.show()
# fig2.show()
# fig3.show()

# import pandas as pd
# import plotly.graph_objects as go
# import plotly.express as px

# # Load the data from CSV file
# data = pd.read_csv("calories_data.csv")

# # Plot 1: Calories Consumed Over Time (Line Chart)
# fig1 = px.line(data, title='Calories Consumed Over Time')
# fig1.update_xaxes(title_text='Entry Number')
# fig1.update_yaxes(title_text='Calories')
# fig1.add_scatter(x=data.index, y=data['Calories'], mode='lines', name='Calories')

# # Plot 2: Distribution of Exercise Duration (Pie Chart)
# exercise_labels = ['< 30 minutes', '30-60 minutes', '> 60 minutes']
# exercise_distribution = data['Exercise'].apply(lambda x: exercise_labels[0] if x < 30 else (exercise_labels[1] if x <= 60 else exercise_labels[2]))
# exercise_counts = exercise_distribution.value_counts()
# fig2 = px.pie(names=exercise_counts.index, values=exercise_counts.values, title='Distribution of Exercise Duration')

# # Plot 3: Distribution of Water Intake (Pie Chart)
# water_labels = ['< 1500 ml', '1500-2000 ml', '> 2000 ml']
# water_distribution = data['Water_Intake'].apply(lambda x: water_labels[0] if x < 1500 else (water_labels[1] if x <= 2000 else water_labels[2]))
# water_counts = water_distribution.value_counts()
# fig3 = px.pie(names=water_counts.index, values=water_counts.values, title='Distribution of Water Intake')

# # Display the plots
# fig1.show()
# fig2.show()
# fig3.show()

import plotly.io as pio
pio.renderers.default = 'browser'


import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Load the data from CSV file
data = pd.read_csv("calories_data.csv")

# Remove non-numeric columns
numeric_data = data.drop(columns=['Date'])

# Plot 1: Calories Consumed and Exercise Over Time (Line Chart)
fig1 = px.line(data, x='Date', y=['Calories', 'Exercise'], title='Calories Consumed and Exercise Over Time')
fig1.update_xaxes(title_text='Date')
fig1.update_yaxes(title_text='Value')

# Plot 2: Water Intake Over Time (Bar Chart)
fig2 = px.bar(data, x='Date', y='Water_Intake', title='Water Intake Over Time')
fig2.update_xaxes(title_text='Date')
fig2.update_yaxes(title_text='Water Intake (ml)')

# Plot 3: Macronutrients Distribution (Pie Chart)
fig3 = go.Figure(data=[
    go.Pie(labels=['Protein', 'Carbs', 'Fat'], values=data[['Protein', 'Carbs', 'Fat']].sum(), hole=0.3)
])
fig3.update_layout(title='Macronutrients Distribution')

# Plot 4: Calories vs Exercise (Scatter Plot)
fig4 = px.scatter(data, x='Exercise', y='Calories', title='Calories vs Exercise', trendline='ols')
fig4.update_xaxes(title_text='Exercise (minutes)')
fig4.update_yaxes(title_text='Calories')

# Plot 5: Correlation Heatmap (excluding non-numeric columns)
fig5 = px.imshow(numeric_data.corr(), x=numeric_data.columns, y=numeric_data.columns, title='Correlation Heatmap')

# Display the plots
fig1.show()
fig2.show()
fig3.show()
fig4.show()
fig5.show()

