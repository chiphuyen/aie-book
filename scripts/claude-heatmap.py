convo_folder = '.' # change to where your exported Claude conversations folder is 
local_tz = 'Asia/Kolkata' # change to your local timezone
# pytz.all_timezones # uncomment to see a list of all supported timezones

import json
import pytz
from datetime import datetime, timezone, timedelta
import matplotlib.dates as mdates
import matplotlib.patches as patches
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter

def load_claude_conversations(file_path):
    """Load and parse Claude conversation data"""
    with open(file_path, 'r') as f:
        convs = json.load(f)
    return convs

def parse_conversation_times(conversations, timezone_name):
    """Extract and convert conversation timestamps to the specified timezone"""
    convo_times = []
    for conv in conversations:
        # Assuming the timestamp is in ISO format or similar
        # Modify this part based on actual Claude data format
        timestamp = conv.get('created_at') or conv.get('timestamp')
        if timestamp:
            # Convert to UTC datetime first
            try:
                # Try parsing ISO format
                utc_datetime = datetime.fromisoformat(timestamp.replace('Z', '+00:00'))
            except:
                # If timestamp is Unix timestamp (as integer or float)
                try:
                    utc_datetime = datetime.fromtimestamp(float(timestamp), tz=timezone.utc)
                except:
                    continue
            
            # Convert to local timezone
            local_datetime = utc_datetime.astimezone(pytz.timezone(timezone_name))
            convo_times.append(local_datetime)
    return convo_times

def create_year_heatmap(convo_times, year):
    """Create a GitHub-style heatmap for Claude conversations"""
    # Convert convo_times to dates and filter for the given year
    just_dates = [convo.date() for convo in convo_times if convo.year == year]
    
    if not just_dates:
        print(f"No conversations found for year {year}")
        return

    date_counts = Counter(just_dates)

    # Create a full year date range for the calendar
    start_date = datetime(year, 1, 1).date()
    end_date = datetime(year, 12, 31).date()

    total_days = (end_date - start_date).days + 1
    date_range = [start_date + timedelta(days=i) for i in range(total_days)]

    # Prepare data for plotting
    data = []
    for date in date_range:
        week = ((date - start_date).days + start_date.weekday()) // 7
        day_of_week = date.weekday()
        count = date_counts.get(date, 0)
        data.append((week, day_of_week, count))

    weeks_in_year = (end_date - start_date).days // 7 + 1

    # Plot the heatmap
    plt.figure(figsize=(15, 8))
    ax = plt.gca()
    ax.set_aspect('equal')

    max_count_date = max(date_counts, key=date_counts.get) if date_counts else start_date
    max_count = date_counts[max_count_date] if date_counts else 0
    counts = list(date_counts.values())
    p90_count = np.percentile(counts, 90) if counts else 1

    # Create heatmap cells
    for week, day_of_week, count in data:
        color = plt.cm.Purples((count + 1) / p90_count) if count > 0 else 'lightgray'
        rect = patches.Rectangle((week, day_of_week), 1, 1, linewidth=0.5, 
                               edgecolor='black', facecolor=color)
        ax.add_patch(rect)

    # Add month labels
    month_starts = [start_date + timedelta(days=i) for i in range(total_days)
                   if (start_date + timedelta(days=i)).day == 1]
    for month_start in month_starts:
        week = (month_start - start_date).days // 7
        plt.text(week + 0.5, 7.75, month_start.strftime('%b'), 
                ha='center', va='center', fontsize=10, rotation=0)

    # Customize appearance
    ax.set_xlim(-0.5, weeks_in_year + 0.5)
    ax.set_ylim(-0.5, 8.5)
    plt.title(
        f'{year} Claude Conversation Heatmap (total={sum(date_counts.values())})\n'
        f'Most active day: {max_count_date} with {max_count} conversations',
        fontsize=16
    )
    plt.xticks([])
    plt.yticks(range(7), ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])
    plt.gca().invert_yaxis()
    
    # Add a colorbar legend
    if counts:
        sm = plt.cm.ScalarMappable(cmap=plt.cm.Purples, 
                                  norm=plt.Normalize(vmin=0, vmax=max_count))
        plt.colorbar(sm, label='Conversations per day')
    
    plt.tight_layout()
    plt.show()

def main():
    # Load conversations
    convs = load_claude_conversations(f'{convo_folder}/conversations.json')
    
    # Parse conversation times
    convo_times = parse_conversation_times(convs, local_tz)
    
    # Create heatmap for current year
    #current_year = datetime.now().year
    current_year = 2025
    create_year_heatmap(convo_times, current_year)

if __name__ == "__main__":
    main()
