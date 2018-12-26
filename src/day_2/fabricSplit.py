from collections import defaultdict


class FabricTracker():
    """
    Class that tracks whether claims have been made for part of the fabric. 

    Two properties 
        shared: Set of tuples (x,y) coordinates discovered that two or more 
        claims are made for

        claimed: Set of tuples (x,y) coordinates discovered only 1 elf 
        wants to use 
    """

    shared = set()
    claimed = defaultdict(list)
    intact_tickets = set()

    
    def __init__(self):
        pass

    def check_claim_intact(self, claim_list: [(int,int)])->[int]:
        """
        Checks if a list of claims has any collisions with other claims and 
        returns the colliding list of claims 

        Args:
            claim_tile: (int,int) Tuple x coordinate, and y coordinate 
            indicating a tile an elf would like to claim.

        Returns
            list of claims that collide with this ticket
        """
        colliding_claims = []
        for claim in claim_list:
            if claim in self.claimed:
                colliding_claims.extend(self.claimed[claim])
        return list(set(colliding_claims))

    def make_claim(self, claim_tile: (int,int), claim_id: int):
        """
        Takes in a tuple of integers that indicate which coordinates of fabric 
        an elf wants to claim and inserts this tile into one of the tracking 
        attributes. If a claim for a coordinate has already been made the 
        coordinate is added to the multi-claim tracking set

        Args:
            claim_tile: (int,int) Tuple x coordinate, and y coordinate 
            indicating a tile an elf would like to claim.
        """
        if claim_tile in self.claimed:
            if claim_tile not in self.shared:
                self.shared.add(claim_tile)
        self.claimed[claim_tile].append(claim_id)

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
    
    def make_multiple_claims(self, claim_list: [(int,int)], claim_id: int):
        """
        Takes in a list of claims and updates the tracking sets
        """
        claim_collision = self.check_claim_intact(claim_list)
        if len(claim_collision) > 0:
            for collision in claim_collision:
                if collision in self.intact_tickets:
                    self.intact_tickets.remove(collision)
        else:
            self.intact_tickets.add(claim_id)
        for claim in claim_list:
            self.make_claim(claim, claim_id)

def generate_claim_dimensions(claim: str)->[int]:
    """
    Takes in a string of a claim made by an elf and extracts data needed to 
    generate the claim coordinates

    Args:
        claim: str In format "#<int> @ <x_offset>,<y_offset>: <width>x<length>"
    Returns:
        list of integers which are the inputs to generate claim coordinates.
    """
    id = claim.split('#')[1].split('@')[0].strip()
    split_at = claim.split('@')[1]
    split_x_offset = split_at.split(',')
    x_offset = split_x_offset[0].strip()
    split_y_offset = split_x_offset[1].split(':')
    y_offset = split_y_offset[0].strip()
    split_dimensions = split_y_offset[1].split('x')
    return [int(x_offset), int(y_offset), int(split_dimensions[0].strip()), int(split_dimensions[1].strip()), id]