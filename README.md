
# Delete WooCommerce Users Script

This Python script allows you to delete all users (customers) from your WooCommerce store, excluding the 'Admin' user. The script utilizes the WooCommerce API to interact with your store and perform the deletion process.

## Prerequisites

Before running the script, make sure you have the following:

- Python 3 installed on your system.
- WooCommerce API credentials (URL, consumer key, and consumer secret) for your WooCommerce store.
- Environment variables set for the WooCommerce API credentials (`WOO_URL`, `WOO_KEY`, `WOO_SECRET`).

## Installation

1. Clone this repository or download the script file (`delete_users.py`) to your local machine.

2. Install the required dependencies using pip:

   ```shell
   pip install woocommerce
   ```

## Usage

1. Set the required environment variables for the WooCommerce API credentials:

   ```shell
   export WOO_URL="https://your-woocommerce-store.com"
   export WOO_KEY="your-consumer-key"
   export WOO_SECRET="your-consumer-secret"
   ```

2. Open a terminal or command prompt and navigate to the directory where the script is located.

3. Run the script:

   ```shell
   python delete_users.py
   ```

   The script will connect to your WooCommerce store using the provided API credentials, retrieve all customers, and delete all users except the 'Admin' user.

## Customization

- If your WooCommerce API credentials are not set as environment variables, you can modify the script and assign the credentials directly to the `url`, `consumer_key`, and `consumer_secret` variables in the script file.

- The script uses the `woocommerce` Python package. If you need to customize the WooCommerce API settings (e.g., API version, authentication method), you can refer to the package documentation for more information: [woocommerce Python package](https://pypi.org/project/woocommerce/).

- The script currently assumes the 'Admin' user has the exact username 'Admin'. If your 'Admin' user has a different username, you can modify the script and update the comparison accordingly.

## License

This script is licensed under the [MIT License](LICENSE).
```

Feel free to copy and paste the above content into your README.md file. You can further customize it as per your requirements.