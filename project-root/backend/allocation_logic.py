import pandas as pd

def load_csv(file_path):
    data = pd.read_csv(file_path)
    return data

def allocate_rooms(group_info, hostel_info):
    allocated_rooms = []
    
    for group_index, group_row in group_info.iterrows():
        group_id = group_row['Group ID']
        group_size = group_row['Number of Members']
        group_gender = group_row['Gender']
        
        group_allocation = {'Group ID': group_id}
        
        for hostel_index, hostel_row in hostel_info.iterrows():
            if group_gender == hostel_row['Gender Accommodation'] and group_size <= hostel_row['Capacity']:
                group_allocation['Hostel Name'] = hostel_row['Hostel Name']
                group_allocation['Room Number'] = hostel_row['Room Number']
                group_allocation['Number of Members'] = group_size
                
                allocated_rooms.append(group_allocation)
                break
    
    return allocated_rooms

def generate_allocation_csv(allocated_rooms):
    df = pd.DataFrame(allocated_rooms)
    df.to_csv('allocation_results.csv', index=False)

group_info = load_csv('data/group_info.csv')
hostel_info = load_csv('data/hostel_info.csv')

allocated_rooms = allocate_rooms(group_info, hostel_info)
generate_allocation_csv(allocated_rooms)