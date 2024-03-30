# -*- coding: utf-8 -*-
"""Artifact.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1w3etk28pbFqrCm_7xnDDksUxwMmbBrws
"""

#Here we import the MusemItem class to inherit from it.
from MuseumItem import MuseumItem

# Artifact class that inherits from MuseumItem
class Artifact(MuseumItem):
    # A constructor of Artifact with parameters for all its attributes and those of MuseumItem.
    def __init__(self, title, artist, dateOfCreation, historicalSignificance,
                 provenance, culturalOrigin, archaeologicalContext,
                 conditionReport, legalStatus, authentication, type):
        #Here we are using the super() to call the constructor of the parent class (MuseumItem).
        super().__init__(title, artist, dateOfCreation, historicalSignificance)
        #It sets the provenance specific to the Artifact
        self.provenance = provenance
        #It sets the cultural origin of the Artifact
        self.culturalOrigin = culturalOrigin
        #It sets the archaeological context of the Artifact
        self.archaeologicalContext = archaeologicalContext
        #It sets the condition report of the Artifact
        self.conditionReport = conditionReport
        #It sets the legal status of the Artifact
        self.legalStatus = legalStatus
        #It sets the authentication details of the Artifact
        self.authentication = authentication
        #It sets the type of the Artifact
        self.type = type

    # Getter method for provenance
    def get_provenance(self):
        return self.provenance

    # Setter method for provenance
    def set_provenance(self, provenance):
        self.provenance = provenance

    # Getter method for cultural origin
    def get_culturalOrigin(self):
        return self.culturalOrigin

    # Setter method for cultural origin
    def set_culturalOrigin(self, culturalOrigin):
        self.culturalOrigin = culturalOrigin

    # Getter method for archaeological context
    def get_archaeologicalContext(self):
        return self.archaeologicalContext

    # Setter method for archaeological context
    def set_archaeologicalContext(self, archaeologicalContext):
        self.archaeologicalContext = archaeologicalContext

    # Getter method for condition report
    def get_conditionReport(self):
        return self.conditionReport

    # Setter method for condition report
    def set_conditionReport(self, conditionReport):
        self.conditionReport = conditionReport

    # Getter method for legal status
    def get_legalStatus(self):
        return self.legalStatus

    # Setter method for legal status
    def set_legalStatus(self, legalStatus):
        self.legalStatus = legalStatus

    # Getter method for authentication
    def get_authentication(self):
        return self.authentication

    # Setter method for authentication
    def set_authentication(self, authentication):
        self.authentication = authentication

    # Getter method for the type of Artifact
    def get_type(self):
        return self.type

    # Setter method for the type of Artifact
    def set_type(self, type):
        self.type = type