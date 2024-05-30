from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker



engine = create_engine('sqlite:///linguist.db')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()




class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)
    decks = relationship('Deck', back_populates='user')

class Deck(Base):
    __tablename__ = 'decks'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates='decks')
    cards = relationship('Card', back_populates='deck')

class Card(Base):
    __tablename__ = 'cards'
    id = Column(Integer, primary_key=True)
    deck_id = Column(Integer, ForeignKey('decks.id'))
    word = Column(String)
    translation = Column(String)
    tip = Column(String)
    deck = relationship('Deck', back_populates='cards')

Base.metadata.create_all(engine)





def user_create(name, email, password):

    user = User(name=name, email=email, password=password)
    session.add(user)
    session.commit()
    return user

def user_get_by_id(user_id):

    return session.query(User).filter_by(id=user_id).first()

def user_update_name(user_id, name):

    user = user_get_by_id(user_id)
    if user:
        user.name = name
        session.commit()
    return user

def user_change_password(user_id, old_password, new_password):

    user = user_get_by_id(user_id)
    if user and user.password == old_password:
        user.password = new_password
        session.commit()
        return True
    return False

def user_delete_by_id(user_id):

    user = user_get_by_id(user_id)
    if user:
        session.delete(user)
        session.commit()
        return True
    return False




def deck_create(name, user_id):

    deck = Deck(name=name, user_id=user_id)
    session.add(deck)
    session.commit()
    return deck

def deck_get_by_id(deck_id):

    return session.query(Deck).filter_by(id=deck_id).first()

def deck_update(deck_id, name):

    deck = deck_get_by_id(deck_id)
    if deck:
        deck.name = name
        session.commit()
    return deck

def deck_delete_by_id(deck_id):

    deck = deck_get_by_id(deck_id)
    if deck:
        session.delete(deck)
        session.commit()
        return True
    return False



def card_create(deck_id, word, translation, tip):

    card = Card(deck_id=deck_id, word=word, translation=translation, tip=tip)
    session.add(card)
    session.commit()
    return card

def card_get_by_id(card_id):

    return session.query(Card).filter_by(id=card_id).first()

def card_filter(sub_word):

    return tuple(session.query(Card).filter(
        (Card.word.contains(sub_word)) |
        (Card.translation.contains(sub_word)) |
        (Card.tip.contains(sub_word))
    ).all())

def card_update(card_id, word=None, translation=None, tip=None):

    card = card_get_by_id(card_id)
    if card:
        if word is not None:
            card.word = word
        if translation is not None:
            card.translation = translation
        if tip is not None:
            card.tip = tip
        session.commit()
    return card

def card_delete_by_id(card_id):

    card = card_get_by_id(card_id)
    if card:
        session.delete(card)
        session.commit()
        return True
    return False
