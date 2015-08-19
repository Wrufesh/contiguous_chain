class Chain(object):

    def __init__(self, c_id, row, start, end):
        self.chain_id = c_id
        self.rows = [(row, (start, end))]

    def edit_row(self, row, start, end):
        for i, rw in enumerate(self.rows):
            if row == rw[0]:
                if end - 2 in range(rw[1][0], rw[1][1]):
                    self.rows[i] = (row, (start, end))
        return self

    def append_row(self, row, start, end):
        self.rows.append((row, (start, end)))
        return self

    @classmethod
    def check_con_upper_row(cls, row, column, chains):
        for chain in chains:
            for item in chain.rows:
                if item[0] == row-1:
                    if column in range(item[1][0], item[1][1]):
                        return True, chain
        return False, None

    @classmethod
    def check_con_left(cls, row, column, chains):
        for chain in chains:
            for item in chain.rows:
                if item[0] == row:
                    if column-1 in range(item[1][0], item[1][1]):
                        return True, item[1][0], chain
        return False, None, None

    @classmethod
    def get_chain_by_id(cls, id, chains):
        for chain in chains:
            if chain.chain_id == id:
                return chain
        return None

    @classmethod
    def update_chains(cls, chains, chain):
        for i, ch in enumerate(chains):
            if ch.chain_id == chain.chain_id:
                chains[i] = chain
        return chains

    @classmethod
    def delete_chain(cls, chains, id):
        for item in chains:
            if item.chain_id == id:
                chains.remove(item)
        return chains

    @classmethod
    def merge(cls, ch, ch1):
        ch.rows = ch.rows + ch1.rows
        return ch


f = open('input.txt', 'r')
data = f.readline().split('\n')[0].split(' ')
i, j = int(data[0]), int(data[1])
chains = []

chain_counter = 1
for p in range(0, i):
    line = f.readline().split('\n')[0]
    for c, t in enumerate(line):
        if t == 'x':
            con_wth_up_row, ch_u = Chain.check_con_upper_row(p, c, chains)
            con_to_left, start, ch_l = Chain.check_con_left(p, c, chains)

            if con_wth_up_row and not con_to_left:
                ch_up = ch_u.append_row(p, c, c + 1)
                chains = Chain.update_chains(chains, ch_up)
            elif con_to_left and not con_wth_up_row:
                ch_lf = ch_l.edit_row(p, start, c + 1)
                chains = Chain.update_chains(chains, ch_lf)

            elif con_to_left and con_wth_up_row:
                if ch_u.chain_id == ch_l.chain_id:
                    chn = Chain.get_chain_by_id(ch_u.chain_id, chains)
                    ch_side = ch_u.edit_row(p, start, c + 1)
                    chains = Chain.update_chains(chains, ch_side)
                else:
                    merged_chain = Chain.merge(ch_u, ch_l)
                    chains = Chain.delete_chain(chains, ch_u.chain_id)
                    chains = Chain.delete_chain(chains, ch_l.chain_id)
                    m_ch = merged_chain.edit_row(p, start, c + 1)
                    chains.append(m_ch)

            elif not con_wth_up_row and not con_to_left:
                ch_id = chain_counter
                new_ch = Chain(ch_id, p, c, c + 1)
                chains.append(new_ch)
                chain_counter += 1
# Output
total_chains = len(chains)
print total_chains
