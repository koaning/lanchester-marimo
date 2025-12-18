## Lanchester Square Law (Aimed Fire)

Two opposing forces are modeled as functions of time:

$$\frac{dA(t)}{dt} = -\beta B(t)$$
$$\frac{dB(t)}{dt} = -\alpha A(t)$$

where $\alpha,\beta > 0$ are effectiveness coefficients.

---

## Deriving the Conserved Quantity

Multiply the first equation by $\alpha A(t)$:

$$\alpha A(t)\frac{dA(t)}{dt} = -\alpha\beta A(t)B(t)$$

Multiply the second equation by $\beta B(t)$:

$$\beta B(t)\frac{dB(t)}{dt} = -\alpha\beta A(t)B(t)$$

Subtracting the second from the first gives:

$$\alpha A(t)\frac{dA(t)}{dt} - \beta B(t)\frac{dB(t)}{dt} = 0$$

---

## Interpreting as a Total Derivative

Using the identities:

$$\frac{d}{dt}\left(A(t)^2\right) = 2A(t)\frac{dA(t)}{dt}$$
$$\frac{d}{dt}\left(B(t)^2\right) = 2B(t)\frac{dB(t)}{dt}$$

we rewrite each term:

$$\alpha A(t)\frac{dA(t)}{dt} = \frac{d}{dt}\left(\frac{\alpha}{2}A(t)^2\right)$$
$$\beta B(t)\frac{dB(t)}{dt} = \frac{d}{dt}\left(\frac{\beta}{2}B(t)^2\right)$$

Substituting back yields:

$$\frac{d}{dt}\left(\frac{\alpha}{2}A(t)^2 - \frac{\beta}{2}B(t)^2\right) = 0$$

Since the time derivative is zero, the quantity is conserved:

$$\alpha A(t)^2 - \beta B(t)^2 = c$$

---

## Applying Initial Conditions

Let the initial forces be:

$$A(0) = A_0$$
$$B(0) = B_0$$

Then the constant is:

$$c = \alpha A_0^2 - \beta B_0^2$$

At the final time $t_f$:

$$\alpha A(t_f)^2 - \beta B(t_f)^2 = \alpha A_0^2 - \beta B_0^2$$

---

## Initial → Final Survivors

Assume combat continues until one force is eliminated.

### A wins

$$\alpha A_0^2 > \beta B_0^2$$

$$B(t_f) = 0$$
$$A(t_f) = \sqrt{A_0^2 - \frac{\beta}{\alpha}B_0^2}$$

### B wins

$$\alpha A_0^2 < \beta B_0^2$$

$$A(t_f) = 0$$
$$B(t_f) = \sqrt{B_0^2 - \frac{\alpha}{\beta}A_0^2}$$

### Mutual annihilation

$$\alpha A_0^2 = \beta B_0^2$$

$$A(t_f) = 0$$
$$B(t_f) = 0$$
