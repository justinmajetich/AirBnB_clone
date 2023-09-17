#!/bin/bash

# Define text formatting codes
GREEN='\033[0;32m'  # Green color
RED='\033[0;31m'    # Red color
NC='\033[0m'         # No color (reset)

#./script6.sh 1> "test_file.txt"
#output=$(cat test_file.txt)
# Capture the provided output
output="$(cat <<EOF
Creating a new State...
Listing all States...
(hbnb)
["[State] (f34956ad-115c-4316-91a1-ce4f91babbb1) {'_sa_instance_state': <sqlalchemy.orm.state.InstanceState object at 0x7f3fb29aef10>, 'name': 'California', 'id': 'f34956ad-115c-4316-91a1-ce4f91babbb1', 'created_at': datetime.datetime(2023, 9, 17, 12, 53, 24), 'updated_at': datetime.datetime(2023, 9, 17, 12, 53, 24)}"]
(hbnb)
Executing SQL query to list all States...
*************************** 1. row ***************************
        id: f34956ad-115c-4316-91a1-ce4f91babbb1
created_at: 2023-09-17 12:53:24
updated_at: 2023-09-17 12:53:24
      name: California
Creating a new City with State ID: f34956ad-115c-4316-91a1-ce4f91babbb1...
(hbnb)
327daed8-7227-4fc9-9772-e66274fdbfde
(hbnb)
Listing all Cities...
(hbnb)
["[City] (327daed8-7227-4fc9-9772-e66274fdbfde) {'_sa_instance_state': <sqlalchemy.orm.state.InstanceState object at 0x7f4ee59a5c50>, 'name': 'San Francisco', 'updated_at': datetime.datetime(2023, 9, 17, 12, 53, 28), 'created_at': datetime.datetime(2023, 9, 17, 12, 53, 28), 'id': '327daed8-7227-4fc9-9772-e66274fdbfde', 'state_id': 'f34956ad-115c-4316-91a1-ce4f91babbb1'}"]
(hbnb)
Creating another City with State ID: f34956ad-115c-4316-91a1-ce4f91babbb1...
(hbnb)
d2fff6ef-d614-4e58-89ed-09eb010ee940
(hbnb)
Executing SQL query to list all Cities...
*************************** 1. row ***************************
        id: 327daed8-7227-4fc9-9772-e66274fdbfde
created_at: 2023-09-17 12:53:28
updated_at: 2023-09-17 12:53:28
      name: San Francisco
  state_id: f34956ad-115c-4316-91a1-ce4f91babbb1
*************************** 2. row ***************************
        id: d2fff6ef-d614-4e58-89ed-09eb010ee940
created_at: 2023-09-17 12:53:32
updated_at: 2023-09-17 12:53:32
      name: San Jose
  state_id: f34956ad-115c-4316-91a1-ce4f91babbb1
EOF
)"

# Define the expected lines
line1="Dropping hbnb_dev_db database if it exists..."
line2="Executing MySQL setup script..."
line3="State ID: "
line4="Creating a new City with State ID: "

# Function to print in green (success)
print_success() {
  echo -e "${GREEN}$1${NC}"
}

# Function to print in red (error)
print_error() {
  echo -e "${RED}$1${NC}"
}

# Check conditions
if [[ "$output" == *"$line1"* ]]; then
  print_success "Line 1: $line1 (OK)"
else
  print_error "Line 1: $line1 (database dropping error)"
fi

if [[ "$output" == *"$line2"* ]]; then
  print_success "Line 2: $line2 (OK)"
else
  print_error "Line 2: $line2 (database creation error)"
fi

if [[ "$output" =~ $line3([0-9a-fA-F-]+) ]]; then
  uuid="${BASH_REMATCH[1]}"
  print_success "Line 3: State ID: $uuid (OK)"
else
  print_error "Line 3: State ID: Not found"
  exit 1
fi

# Check if the captured UUID matches in subsequent lines
if [[ "$output" == *"state_id: $uuid"* && "$output" == *"Creating a new City with State ID: $uuid"* ]]; then
  print_success "UUID in subsequent lines matches: $uuid (OK)"
else
  print_error "UUID in subsequent lines does not match: $uuid"
  exit 1
fi

# Capture and test the consistency of the two city IDs
city_id1=""
city_id2=""
city_id1_line=""
city_id2_line=""
while read -r line; do
  if [[ "$line" == *"$line4"* ]]; then
    city_id1_line="$line"
    city_id1="$city_id2"  # Update the first city ID with the previous second city ID
    city_id2=""
  elif [[ "$line" =~ ^[0-9a-fA-F-]+$ ]]; then
    if [ -z "$city_id1" ]; then
      city_id1="$line"
      city_id1_line="$line"
    else
      city_id2="$line"
      city_id2_line="$line"
    fi
  fi
done <<< "$output"

echo "city_id1_line $city_id1_line"
echo "city_id2_line $city_id2_line"
echo "city_id1 $city_id1"
echo "city_id2 $city_id2"

echo "OUPUT:"
cat test_file.txt