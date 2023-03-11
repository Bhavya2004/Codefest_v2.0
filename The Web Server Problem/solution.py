# Run the following command to execute the code:
# python solution.py < TWSP_small.txt >TWSP_small_output.txt
# python solution.py < TWSP_large.txt >TWSP_large_output.txt

# Initialize the websites list
websites = []
# Read the number of test cases
T = int(input())

# Define a custom sort function to sort the websites
def sort_websites(website):
    homepage_size = website[0] + website[1]
    return (-homepage_size, -website[0], -website[2])

# Iterate over each test case
for i in range(T):
   # Read the sizes of the text content, images, and forms
    A, B, C = map(int, input().split())


    # Calculate the total size of the homepage
    homepage_size = A + B

    # Append the website to a list
    website = [A, B, C]
    websites.append(website)

# Sort the websites based on their size and priority
websites.sort(key=sort_websites)

# Iterate over each website and calculate the time required to serve the content
for website in websites:
    content_size = website[0] + website[1] + website[2]
    time_required = content_size / (2 * 1024 * 1024)  # in seconds

    # Check if the website can be served within 60 seconds
    if time_required <= 60:
        print(','.join(str(x) for x in website))

