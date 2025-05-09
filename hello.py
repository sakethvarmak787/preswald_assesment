from preswald import text, plotly, connect, get_df, table, query
import pandas as pd
import plotly.express as px

# Load the CSV
connect()
df = pd.read_csv('./data/Dataset_Malawi_National_Football_Team_Matches.csv')

# Correct SQL query
sql = "SELECT * FROM df WHERE Result = 'Loss'"
filtered_df = df[df['Opponent'] == "Kenya"]

# Display results
text("# My Data Analysis App")
table(filtered_df, title="Filtered Data")



fig = px.scatter(df, x='Opponent', y='Opponent Score',
                 title='Quantity vs. Value')

# Add labels for each point
fig.update_traces(textposition='top center', marker=dict(size=12, color='lightblue'))

# Style the plot
fig.update_layout(template='plotly_white')

# Show the plot
plotly(fig)

# Show the data
table(df)