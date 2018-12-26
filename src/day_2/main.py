import sys
import fabricSplit

if __name__ == "__main__":
    roll_fabric = fabricSplit.FabricTracker()
    with open(sys.argv[1]) as f:
        for line in f:
            claim_dims = fabricSplit.generate_claim_dimensions(line)
            roll_fabric.make_multiple_claims(roll_fabric.generate_claims(claim_dims[0], claim_dims[1],claim_dims[2],claim_dims[3]), claim_dims[4])
    print(len(roll_fabric.shared))     
    print(roll_fabric.intact_tickets)   
    