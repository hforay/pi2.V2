import streamlit as st

class Utilisateur:
    def __init__(self, username, prenom, nom, note, access, commentaires, donnees, connection) :
        self.username = username
        self.prenom = prenom
        self.nom = nom
        self.note = note
        self.access = access
        self.commentaires = []
        self.donnees = []
        self.connection = connection

    def getUsername(self):
        return self.username

    def getPrenom(self):
        return self.prenom

    def getNom(self):
        return self.nom

    def getNote(self):
        return self.note

    def getAccess(self):
        return self.access

    def getCommentaires(self):
        return self.commentaires

    def AjoutCom(self, commentaire):
        self.commentaires.append(commentaire)

    def getDonnees(self):
        return self.donnees
