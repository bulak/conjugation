#!/usr/bin/env python3

import random
import sys
from verbecc import inflector_fr


class FrenchTester(object):
    inflector = inflector_fr.InflectorFr()    
    def __init__(self):
        self.verbs = [
            "avoir",
            "être",
            "aller",
            "faire",
            "dire",
            
            "aimer",
            "finir",
            "rendre",
            "savoir",
            "vouloir",

            "pouvoir",
            "manger",
            "lancer",
            "mettre",
            "oublier",
            
            "prendre",
            "sortir",
            "courir",
            "voir",
            "venir",
            
            "employer",
            "payer",
            "acheter",
            "offrir",
            "envoyer"
        ]
        self.tenses = {
            "indicatif": [
                "présent",
                "imparfait",
                "futur-simple",
                # "passé-simple",
                "passé-composé",
                # "plus-que-parfait",
                # "futur-antérieur",
                # "passé-antérieur"
            ],
            "conditionnel": [
                "présent",
                # "passé"
            ],
            # "subjonctif": [
                # "présent",
                # "imparfait",
                # "passé",
                # "plus-que-parfait"
            # ],
            "imperatif": [
                "imperatif-présent",
                # "imperatif-passé"
            ],
            # "participe": [
                # "participe-présent",
                # "participe-passé"
            #]
        }
        self.tense_keys = [
            (k1, k2) for k1 in self.tenses
            for k2 in self.tenses[k1]
        ]
        self.prenoms = {6: [
            "je", "tu", "il",
            "nous", "vous", "ils"
        ],
                        3: [
            "tu", "nous", "vous"
        ]}
                            
    def prepare_test(self, n=30):
        verbs = random.choices(self.verbs, k=n)
        tenses = random.choices(self.tense_keys, k=n)
        for i in range(n):
            conj = self.inflector.conjugate(verbs[i])
            yield (verbs[i], tenses[i],
                   conj["moods"][tenses[i][0]][tenses[i][1]])

def main():
    tester = FrenchTester()
    for verb, tense, answer in tester.prepare_test():
        possible_prenoms = tester.prenoms[len(answer)]
        prenoms = random.sample(possible_prenoms, 2)
        for prenom in prenoms:
            prenom_index = possible_prenoms.index(prenom)
            response = input(
                "'{}' - '{}' - '{}': ".format(
                    verb, "/".join(tense), prenom))
            if response != answer[prenom_index]:
                print("Non! C'est <<{}>>".format(answer[prenom_index]))
    print("Merci. C'est fini. A+")
    _ = input()

if __name__ == "__main__":
    sys.exit(main())
