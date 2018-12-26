


class FabricTracker():
    """
    Class that tracks whether claims have been made for part of the fabric. 

    Two properties 
        shared: Set of tuples (x,y) coordinates discovered that two or more 
        claims are made for

        solo_claimed: Set of tuples (x,y) coordinates discovered only 1 elf 
        wants to use 
    """

    shared = set()
    solo_claimed = set()
    
    def __init__(self):
        pass
    
    def make_claim(self, claim_tile: (int,int)):
        """
        Takes in a tuple of integers that indicate which coordinates of fabric 
        an elf wants to claim and inserts this tile into one of the tracking 
        attributes. If a claim for a coordinate has already been made the 
        coordinate is added to the multi-claim tracking set

        Args:
            claim_tile: (int,int) Tuple x coordinate, and y coordinate 
            indicating a tile an elf would like to claim.
        """
        if claim_tile not in self.solo_claimed:
            self.solo_claimed.add(claim_tile)
        else:
            if claim_tile not in self.shared:
                self.shared.add(claim_tile)
    
    def generate_claims(self, x_offset: int, y_offset: int, width: int, height: int)->[(int,int)]:
        """
        Takes in a claim made by an elf and generates a list of the 
        coordinates the elf would lay claim to

        Args:
            x_offset: int The offset from the left-most position of the fabric 
            sheet 
            y_offset: int The offset from the top-most position of the fabric 
            sheet
            width: int The total width of the claim sheet
            height: int THe total height of the claim sheet

        Returns:
            List of tuples indicating all the parts of the an elf is requesting.
        """
        claims = []
        for x_vals in range(0, width):
            for y_vals in range(0,height):
                claims.append((x_vals+x_offset, y_vals+y_offset))
        return claims