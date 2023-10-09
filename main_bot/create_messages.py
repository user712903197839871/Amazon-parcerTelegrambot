from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import random

# This function allow us to create an HTML message to send
# You can edit all fields of message using HTML syntax

def create_item_html(items):
    response = []
    print(f'{5 * "*"} Creating post {5 * "*"}')

    # Shuffling items
    random.shuffle(items)

    # Iterate over items
    for item in items:
        # If item has an active offer
        if 'off' in item:

            # Creating message body
            html = ""
            html += f"🎁 <b>{item['title']}</b> 🎁\n\n"

            if 'description' in list(item.keys()):
                html += f"{item['description']}\n"

            html += f"<a href='{item['image']}'>&#8205</a>\n"

            if 'savings' in list(item.keys()):
                html += f"❌ No more: {item['original_price']}€ ❌\n\n"

            html += f"💰 <b>At the price of: {item['price']}</b> 💰\n\n"

            if 'savings' in list(item.keys()):
                html += f"✅ <b>Save: {item['savings']}€</b> ✅\n\n"
            print(item)
            
            if 'discount' in list(item.keys()):
                html += f"Save: {item['discount']}% 😳"

            keyboard = [
                [InlineKeyboardButton("🛒 Buy Now 🛒", callback_data='buy', url=item["url"])],
            ]

            # Creating buy button
            reply_markup = InlineKeyboardMarkup(keyboard)
            response.append(html)
            response.append(reply_markup)
    return response
