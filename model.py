def score_employee(overtime, travel, role, marital, years,
                   years_role, years_mgr, income, wlb, dept):
    score = 20

    if overtime == 'Yes':               score += 20
    if travel == 'Travel_Frequently':   score += 12
    if role == 'Sales Representative':  score += 18
    elif role == 'Laboratory Technician': score += 10
    elif role == 'Human Resources':     score += 9
    elif role == 'Manager':             score -= 8
    elif role == 'Research Director':   score -= 10
    elif role == 'Manufacturing Director': score -= 5

    if marital == 'Single':             score += 10

    if years <= 2:                      score += 15
    elif years <= 5:                    score += 7
    elif years >= 15:                   score -= 8

    if years_role <= 1:                 score += 8
    if years_mgr <= 1:                  score += 6

    if income < 4000:                   score += 14
    elif income < 6000:                 score += 6
    elif income >= 12000:               score -= 8

    if wlb == 1:                        score += 12
    elif wlb == 4:                      score -= 5

    if dept == 'Sales':                 score += 5
    elif dept == 'Human Resources':     score += 4

    return min(97, max(3, score))


def get_risk_level(score):
    if score >= 60:   return 'HIGH'
    if score >= 35:   return 'MEDIUM'
    return 'LOW'


def get_drivers(overtime, travel, role, income, years,
                years_role, years_mgr, marital, wlb):
    drivers = []
    if overtime == 'Yes':
        drivers.append(('Overtime', 'HIGH', 'Strong burnout signal — #2 predictor'))
    if role == 'Sales Representative':
        drivers.append(('Sales Representative role', 'HIGH', 'Highest exit rate in dataset (39.8%)'))
    if role == 'Laboratory Technician':
        drivers.append(('Laboratory Technician role', 'HIGH', '23.9% attrition rate'))
    if income < 4000:
        drivers.append((f'Low income (₹{income:,})', 'HIGH', 'Well below avg of leavers (₹4,787)'))
    elif income < 6000:
        drivers.append((f'Below avg income (₹{income:,})', 'MEDIUM', 'Below stayed avg of ₹6,833'))
    if travel == 'Travel_Frequently':
        drivers.append(('Frequent travel', 'MEDIUM', '6th strongest predictor of exit'))
    if years <= 2:
        drivers.append((f'Early tenure ({years} yrs)', 'MEDIUM', 'Peak exit window is years 1–3'))
    if marital == 'Single':
        drivers.append(('Single — higher mobility', 'MEDIUM', '4th strongest predictor'))
    if wlb == 1:
        drivers.append(('Poor work-life balance (rating 1)', 'MEDIUM', '31.2% attrition at rating 1'))
    if years_mgr <= 1:
        drivers.append(('New manager relationship', 'LOW', 'Manager change increases instability'))
    if years_role <= 1:
        drivers.append(('New in current role', 'LOW', 'Low role tenure adds restlessness'))
    return drivers[:5]


def get_recommendation(risk_level):
    if risk_level == 'HIGH':
        return (
            "Schedule a manager check-in this week. "
            "Review compensation against market rate. "
            "Consider a structured 90-day retention plan with clear career milestones."
        )
    if risk_level == 'MEDIUM':
        return (
            "Monitor over the next 30 days. "
            "Consider a career progression conversation and workload review. "
            "Check if overtime load can be reduced."
        )
    return (
        "Employee appears stable. "
        "Continue regular check-ins as part of standard HR practice."
    )
