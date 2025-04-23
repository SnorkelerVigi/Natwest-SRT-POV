from typing import Dict, Tuple, Type, Union, List
from enum import Enum
from pydantic import BaseModel

# Import all the classes defined in the previous code
# This is a reference to those classes, assuming they're imported from a module called 'models'
from response_types import (
    # Enums
    YesNo, DaysBusinessDays, GoverningLaw, SubParticipationCaptureSRT,
    LenderRightConditions, BorrowerConsentConditions, KeyTerms, KeyTermsConditions,
    DisclosureParties, NDARequiredParties, NDAFormType, ConsentRequiredParties,
    NotificationRequiredParties, NDARequirements, DisclosureRestrictions,
    LenderConsentType, PrepaymentWithoutFeeDate,
    
    # Response classes
    BaseResponse, FreeTextResponse, DaysBusinessDaysResponse, GoverningLawResponse, GoverningLawClauseNumberResponse,SubParticipationProvisions, SubParticipationDefined,
    SubParticipationCaptureSRTResponse, LenderRightConditionsResponse,
    BorrowerConsentConditionsResponse, FormOfNoticeSpecified, KeyTermsResponse,
    KeyTermsConditionsResponse, EligibilityForSRT, ConfidentialityProvisions,
    DisclosurePermitted, DisclosurePartiesResponse, NDARequiredPartiesResponse,
    PrescribedNDAForm, NDAFormTypeResponse, NDAFormLMABased, NDAAdditionalConditions,
    ConsentRequiredPartiesResponse, NotificationRequiredPartiesResponse,
    NDARequirementsResponse, DisclosureRestrictionsResponse,
    DisclosurePermittedWithoutConditions, NatwestAffiliatesDisclosure,
    NatwestRepresentativesDisclosure, AdditionalBorrowersProvision,
    LenderConsentTypeResponse, InterestRateFloor, InterestRateFloorNonZero,
    InterestRateCap, PrepaymentFeePayable, PrepaymentAmountPermitted,
    PrepaymentWithoutFeeDateResponse
)

# Define a type for the mapping value
# Each entry will have the Response class and the Enum class if applicable
MappingValue = Tuple[
    Type[BaseResponse],  # Response class
    Union[Type[Enum], List[Type[Enum]], None]  # Enum class(es) or None if free text
]

# Create the mapping from CSV questions to class types
question_to_class_mapping: Dict[str, MappingValue] = {
    # Agreement Details
    "Governing law": (GoverningLawResponse, GoverningLaw),
    "Please detail the clause number of the governing law clause": (GoverningLawClauseNumberResponse, None),  # Free text
    
    # Eligibility Part 1
    "Does the agreement contain express provisions relating to sub-participations by Lenders?": (SubParticipationProvisions, YesNo),
    "Is sub-participation defined?": (SubParticipationDefined, YesNo),
    "Please set out the relevant definition of sub-participation (including clause reference)": (FreeTextResponse, None),  # Free text
    "Does the definition of sub-participation capture SRT?": (SubParticipationCaptureSRTResponse, SubParticipationCaptureSRT),
    "Select what conditions apply to the Lender's right to sub-participate": (LenderRightConditionsResponse, LenderRightConditions),
    "Please detail what restrictions apply": (FreeTextResponse, None),  # Free text
    "What other conditions apply?": (FreeTextResponse, None),  # Free text
    "Select all conditions that apply to Borrower's/Parent's/Obligors' consent": (BorrowerConsentConditionsResponse, BorrowerConsentConditions),
    "What other conditions apply?": (FreeTextResponse, None),  # Free text
    "Number of days for deemed consent": (FreeTextResponse, None),  # Free text/numeric
    "Is this in days or Business Days?": (DaysBusinessDaysResponse, DaysBusinessDays),
    "How many days notice to the Borrower/Parent/Obligors are required?": (FreeTextResponse, None),  # Free text/numeric
    "Is the notice period in days or Business Days?": (DaysBusinessDaysResponse, DaysBusinessDays),
    "Is a form of notice specified?": (FormOfNoticeSpecified, YesNo),
    "Please detail the form of notice required": (FreeTextResponse, None),  # Free text
    "Number of days required for consultation": (FreeTextResponse, None),  # Free text/numeric
    
    # Eligibility Part 2
    "Do any of the following key terms appear anywhere in the agreement, other than in the definition of sub-participation?": (KeyTermsResponse, KeyTerms),
    "Please detail the relevant provision and clause number": (FreeTextResponse, None),  # Free text
    "Are there any conditions which apply to the provisions containing those key terms?": (KeyTermsConditionsResponse, KeyTermsConditions),
    "Please detail what restrictions apply": (FreeTextResponse, None),  # Free text
    "What other conditions apply?": (FreeTextResponse, None),  # Free text
    "Select all conditions that apply to Borrower's/Parent's/Obligors' consent": (BorrowerConsentConditionsResponse, BorrowerConsentConditions),
    "What other conditions apply?": (FreeTextResponse, None),  # Free text
    "Number of days for deemed consent": (FreeTextResponse, None),  # Free text/numeric
    "Is this in days or Business Days?": (DaysBusinessDaysResponse, DaysBusinessDays),
    "How many days notice to the Borrower/Parent/Obligors are required?": (FreeTextResponse, None),  # Free text/numeric
    "Is the notice period in days or Business Days?": (DaysBusinessDaysResponse, DaysBusinessDays),
    "Is a form of notice specified?": (FormOfNoticeSpecified, YesNo),
    "Please detail the form of notice required": (FreeTextResponse, None),  # Free text
    "Number of days required for consultation": (FreeTextResponse, None),  # Free text/numeric
    
    # Many similar pattern questions follow with same structure...
    
    # Eligibility Summary
    "Based on the questions in section Eligibiliy Part 1 and section Eligibility Part 2 above, please confirm if the facility you are reviewing can be included in a SRT without restrictions or conditions": (EligibilityForSRT, YesNo),
    "Please provide further details": (FreeTextResponse, None),  # Free text
    
    # Confidentiality and Disclosure
    "Does the agreement contain confidentiality/disclosure provisions?": (ConfidentialityProvisions, YesNo),
    "Please insert the relevant clause": (FreeTextResponse, None),  # Free text
    "Is disclosure expressly permitted to any persons entering or potentially entering into transaction under which payments are to be made or may be made by reference to one or more Finance Documents (with or without restriction)?": (DisclosurePermitted, YesNo),
    "Please set out the relevant provision including clause reference": (FreeTextResponse, None),  # Free text
    "Is disclosure expressly permitted to any of the following parties in so far as they relate to any persons entering of potentially entering into transaction under which payments are made or may be made by reference to one or more Finance Documents (with or without restriction)?": (DisclosurePartiesResponse, DisclosureParties),
    "Is a confidentiality undertaking/other form of NDA required to disclose to any of these parties?": (NDARequiredPartiesResponse, NDARequiredParties),
    "Please set out the relevant definition of \"Confidentiality Undertaking\"": (FreeTextResponse, None),  # Free text
    "Is there a prescribed form of confidentiality undertaking / other form of NDA?": (PrescribedNDAForm, YesNo),
    "What form of confidentiality undertaking/other form of NDA is specified?": (NDAFormTypeResponse, NDAFormType),
    "Is the form of confidentiality undertaking substantially in a recommended form of the LMA?": (NDAFormLMABased, YesNo),
    "Is the definition of Confidentiality Undertaking substantially in a recommended form of the LMA?": (NDAFormLMABased, YesNo),
    "Does the definition of \"Confidentiality Undertaking\" expressly include any other conditions?": (NDAAdditionalConditions, YesNo),
    "Please detail any additional conditions which apply": (FreeTextResponse, None),  # Free text
    "Is Borrower/Obligor/Parent consent required to disclose to any of these parties?": (ConsentRequiredPartiesResponse, ConsentRequiredParties),
    "Please set out the relevant consent provision including clause reference": (FreeTextResponse, None),  # Free text
    "Is there a requirement for the Borrower, Obligor, Parent to be notified in order for disclosure of confidential information to be permitted to any of these parties?": (NotificationRequiredPartiesResponse, NotificationRequiredParties),
    "Please set out the relevant notification provision including clause reference": (FreeTextResponse, None),  # Free text
    "If a confidentiality undertaking / other form of NDA is required, is there any requirement to obtain consent from and/ or notify any party in relation to that undertaking/ NDA?": (NDARequirementsResponse, NDARequirements),
    "Please set out the relevant consent provision including clause reference.": (FreeTextResponse, None),  # Free text
    "Is there any restriction in the confidentiality or in the assignment and transfer provisions which prevents the Lender from dicslosing information to any of the following?": (DisclosureRestrictionsResponse, DisclosureRestrictions),
    "Please set out the relevant restriction including clause reference.": (FreeTextResponse, None),  # Free text
    "Ignoring any requirement for a confidentiality undertaking substantially in a form recommended by the LMA, is disclosure expressly permitted to persons [potentially] entering into a transaction under which payments are made/may be made without conditions": (DisclosurePermittedWithoutConditions, YesNo),
    "Is disclosure expressly permitted to any Affiliates to National Westminster Bank Plc without restriction or any conditions?": (NatwestAffiliatesDisclosure, YesNo),
    "Please detail any restrictions or conditions which apply": (FreeTextResponse, None),  # Free text
    "Is disclosure expressly permitted to any Representatives to National Westminster Bank Plc without restriction or any conditions?": (NatwestRepresentativesDisclosure, YesNo),
    "Please detail any restrictions or conditions which apply.": (FreeTextResponse, None),  # Free text
    "Please set out the relevant definition of \"Representatives\"": (FreeTextResponse, None),  # Free text
    
    # Additional Borrowers
    "Does the agreement provide for the accession of Additional Borrowers?": (AdditionalBorrowersProvision, YesNo),
    "Does the accession of additional Borrowers require Lender Consent?": (LenderConsentTypeResponse, LenderConsentType),
    "Please provide details of the relevant requirements": (FreeTextResponse, None),  # Free text
    
    # Interest Rate Provisions
    "Does the facility contain an interest rate floor?": (InterestRateFloor, YesNo),
    "Is the interest rate floor set at a rate other than zero?": (InterestRateFloorNonZero, YesNo),
    "Please set out the relevant rate": (FreeTextResponse, None),  # Free text
    "Does the facility contain an interest rate cap?": (InterestRateCap, YesNo),
    "Please specify the interest rate cap/Please provide further details.": (FreeTextResponse, None),  # Free text
    
    # Prepayment Fee
    "Is a charge or fee payable on prepayments (whether full or partial)?": (PrepaymentFeePayable, YesNo),
    "Prepayments permitted up to certain amount per year before charges?": (PrepaymentAmountPermitted, YesNo),
    "What is the threshold of prepayments permitted before charges are incurred?": (FreeTextResponse, None),  # Free text
    "Is there a date after which borrower can make prepayments without fee or penalty?": (PrepaymentWithoutFeeDateResponse, PrepaymentWithoutFeeDate),
    "Date after which borrower can make prepayments without fee or penalty": (FreeTextResponse, None),  # Free text
    "What prepayment fees are payable?": (FreeTextResponse, None),  # Free text
    "Please detail the relevant clause which governs the payment of a prepayment fee": (FreeTextResponse, None)  # Free text
}

# Function to get the appropriate class for a given question
def get_classes_for_question(question_text: str) -> MappingValue:
    """
    Get the appropriate response class and enum class for a given question.
    
    Args:
        question_text: The exact text of the question from the CSV
        
    Returns:
        A tuple of (response_class, enum_class) or (None, None) if it's a free text field
    """
    return question_to_class_mapping.get(question_text, (None, None))