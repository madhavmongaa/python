# ── driver_dispatch.py (RideSurge Technologies · Core Dispatch Module) ──
# Business rules (Ops Manual v5.1):
# Rule A: Driver can accept a PREMIUM ride ONLY IF all three hold:
# rating >= 4.7 AND trips_completed >= 200 AND car_type == "sedan"
# Rule B: SURGE pricing fires when the rider/driver ratio is AT LEAST 3 (>= 3)
# AND it is currently raining.
# Rule C: FREE-RIDE coupon issued when customer is a new user AND at least one
# of: (referral code used) OR (promo is active).
# Existing users are NOT eligible, even if a promo is running.

driver_rating = 4.8
trips_completed = 150  # below the required 200-trip threshold
car_type = "sedan"

active_riders = 114  # exactly 3 times active_drivers
active_drivers = 38
rain = True

is_new_user = False  # this is a returning customer, not a new one
referral_code = ""
promo_active = True

# Rule A — Premium ride eligibility
# Used AND instead of OR to ensure all three conditions must be true for premium eligibility.
can_take_premium = (
    driver_rating >= 4.7 and trips_completed >= 200 and car_type == "sedan"
)

# Rule B — Surge pricing
#Used AND instead of OR to ensure both conditions must be true for surge pricing to be active.
surge_active = (active_riders / active_drivers) >= 3 and rain == True

# Rule C — Free-ride coupon
#Used AND and OR to ensure that the user is new and at least one of the other conditions is true for free-ride coupon eligibility.
free_ride_coupon = is_new_user and (referral_code != "" or promo_active)

print("Premium eligible:", can_take_premium)
print("Surge active: ", surge_active)
print("Free ride coupon:", free_ride_coupon)