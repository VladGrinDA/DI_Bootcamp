# DNA

import random

class Gene:
    def __init__(self, value=None) -> None:
        self.value = random.randint(0, 1) if not value else value

    def mutate(self):
        self.value = int((self.value + 1) % 2)

    def __repr__(self):
        return str(self.value)

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, Gene):
            return self.value == value
        return self.value == value.value


class MutatableCollection:
    def __init__(self, mutatable_object, collection_lenght, mutate_prob) -> None:
        self.collection = [mutatable_object() for _ in range(collection_lenght)]
        self.mutate_prob = mutate_prob

    def mutate(self):
        for object in self.collection:
            if random.random() <= self.mutate_prob:
                object.mutate()

    def __iter__(self):
        return iter(self.collection)

class Chromosome(MutatableCollection):
    def __init__(self) -> None:
        super().__init__(Gene, 10, 0.5)

    def __repr__(self):
        return ' '.join([str(gene) for gene in self])

    def genes(self):
        return self.collection
    
class DNA(MutatableCollection):
    def __init__(self) -> None:
        super().__init__(Chromosome, 10, 0.5)

    def __repr__(self):
        return '\n'.join([str(chromosome) for chromosome in self])
    
    def chromosomes(self):
        return self.collection
    

class Organism:
    def __init__(self, enviroment) -> None:
        self.dna = DNA()
        self.enviroment = enviroment

    def mutate(self):
        if random.random() <= self.enviroment['mutate_prob']:
            self.dna.mutate()

    def genes(self):
        return list(map(lambda x: x.genes(), self.chromosomes()))

    def chromosomes(self):
        return self.dna.chromosomes()
    
    def all_genes_ones(self):
        return all([all(map(lambda gene: gene == 1, chromosome)) for chromosome in self.dna])
    

def experiment():
    enviroment = {
        'mutate_prob': 1
    }
    n_organisms = 1
    organisms = [Organism(enviroment) for _ in range(n_organisms)]
    all_ones = False
    n_iter = 0

    while not all_ones and n_iter < 1e8:
        for organism in organisms:
            if n_iter % 1e3 == 0: 
                print('generation', n_iter, end='\r')
            if organism.all_genes_ones():
                all_ones = True
                break
            organism.mutate()
            n_iter += 1
    
    if all_ones:
        print(f"It took {n_iter} generations for {n_organisms} organisms to get a DNA be composed of only 1")
    else:
        print("Number if iterations exceeded the upper limit")


def test_all_ones():
    organism = Organism({'mutate_prob': 1})

    gene = Gene()
    gene.value = 1

    chromosome = Chromosome()
    chromosome.collection = [gene for _ in range(10)]

    dna = DNA()
    dna.collection = [chromosome for _ in range(10)]

    organism.dna = dna

    print(organism.dna)
    print(organism.all_genes_ones())

    gene.mutate()
    print(organism.dna)
    print(organism.all_genes_ones())

def test_mutates():
    print('gene')
    gene = Gene()
    print(gene.value)
    gene.mutate()
    print(gene.value)
    gene.mutate()
    print(gene.value)

    print('chromosome')
    chromosome = Chromosome()
    print(chromosome)
    chromosome.mutate()
    print(chromosome)
    chromosome.mutate()
    print(chromosome)

    print('dna')
    dna = DNA()
    print(dna)
    dna.mutate()
    print('after mutation')
    print(dna)

    print('organism')
    organism = Organism({'mutate_prob': 1})
    print(organism.dna)
    print(organism.all_genes_ones())
    organism.mutate()
    print('after mutation')
    print(organism.dna)
    print(organism.all_genes_ones())


if __name__ == '__main__':
    experiment()
    # test_all_ones()
    # test_mutates()



