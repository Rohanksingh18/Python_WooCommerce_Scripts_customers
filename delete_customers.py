
import os
from woocommerce import API
import logging as logger

# WooCommerce API credentials
url = os.environ.get('WOO_URL')
consumer_key = os.environ.get('WOO_KEY')
consumer_secret = os.environ.get('WOO_SECRET')

# Initialize WooCommerce API (Payload)
wcapi = API(
    url=url,
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    wp_api=True,
    version="wc/v3"
)


def delete_all_users_except_admin():
    total_users = 0
    deleted_users = 0

    # Define pagination parameters (default per_page is 10)
    page = 1
    per_page = 100  # Adjust the value based on your needs

    while True:
        # Retrieve users using pagination
        users = wcapi.get("customers", params={"page": page, "per_page": per_page}).json()

        if not users:
            break  # No more users to retrieve, exit the loop

        total_users += len(users)

        # Iterate over each user
        for user in users:
            user_id = user["id"]
            username = user["username"]

            if username == 'Admin':
                logger.info("Skipping 'Admin' user")
                continue

            # Delete the user
            wcapi.delete("customers/{}".format(user_id), params={"force": True})
            deleted_users += 1

        page += 1  # Move to the next page

    # Calculate remaining users
    remaining_users = total_users - deleted_users

    # Print the summary
    print("Summary:")
    logger.info("Printing total number of users")
    print("Total users: {}".format(total_users))
    logger.info("Printing total number of deleted users")
    print("Deleted users: {}".format(deleted_users))
    logger.info("Printing total number of remaining users")
    print("Remaining users: {}".format(remaining_users))


# Call the function to delete all users except 'Admin'
delete_all_users_except_admin()
