import linguist

user = linguist.user_create("Alice", "alice@example.com", "password123")
assert user.name == "Alice"
assert user.email == "alice@example.com"

retrieved_user = linguist.user_get_by_id(user.id)
assert retrieved_user.name == "Alice"

updated_user = linguist.user_update_name(user.id, "Alice Smith")
assert updated_user.name == "Alice Smith"

assert linguist.user_change_password(user.id, "password123", "newpassword123")

assert linguist.user_delete_by_id(user.id)

user = linguist.user_create("Bob", "bob@example.com", "password123")
deck = linguist.deck_create("French Basics", user.id)
assert deck.name == "French Basics"

retrieved_deck = linguist.deck_get_by_id(deck.id)
assert retrieved_deck.name == "French Basics"

updated_deck = linguist.deck_update(deck.id, "Advanced French")
assert updated_deck.name == "Advanced French"

assert linguist.deck_delete_by_id(deck.id)

deck = linguist.deck_create("Spanish Basics", user.id)
card = linguist.card_create(deck.id, "Hello", "Hola", "Greetings")
assert card.word == "Hello"

retrieved_card = linguist.card_get_by_id(card.id)
assert retrieved_card.word == "Hello"

filtered_cards = linguist.card_filter("Hello")
assert len(filtered_cards) > 0


updated_card = linguist.card_update(card.id, word="Hi", translation="Hola", tip="Informal greeting")
assert updated_card.word == "Hi"


assert linguist.card_delete_by_id(card.id)


linguist.user_delete_by_id(user.id)

