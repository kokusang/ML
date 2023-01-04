                import numpy as np
                u = np.random.choice([0,1], 100000)
                v = np.random.choice([0,1], 100000)
                u[:50000] = v[:50000]
                sum(u==v)/float(len(u)) # -> you get 0.75
                np.mean(np.abs(u-v)) # -> you get 0.25