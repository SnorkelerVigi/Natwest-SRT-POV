import enum
from typing import List

from enum import Enum
from typing import List, Optional, Union
from pydantic import BaseModel, Field


# Base Response Model
class BaseResponse(BaseModel):
    """Base model for all checklist responses.

    Attributes:
        rationale: The explanation for the response and the rationale for the response
        # clause_number: The clause number(s) referred to in the response
        # clause_text_verbatim: The exact text of the clause or clauses being used to frame the response
    """
    rationale: str
    clause_number: List[str] = Field(default_factory=list)
    clause_text_verbatim: List[str] = Field(default_factory=list)

class FreeTextResponse(BaseResponse):
    """Response for free text questions."""
    response: str

# Common Enums
class YesNo(Enum):
    YES = "Yes"
    NO = "No"


class DaysBusinessDays(Enum):
    DAYS = "Days"
    BUSINESS_DAYS = "Business Days"


# Agreement Details Enums and Models
class GoverningLaw(Enum):
    NOT_SPECIFIED = "Not Specified"
    ENGLAND_AND_WALES = "England and Wales"
    SCOTLAND = "Scotland"
    NORTHERN_IRELAND = "Northern Ireland"
    UNITED_STATES = "United States"
    AFGHANISTAN = "Afghanistan"
    ALBANIA = "Albania"
    ALGERIA = "Algeria"

class DaysBusinessDaysResponse(BaseResponse):
    """Response for days or business days question."""
    response: DaysBusinessDays

class GoverningLawResponse(BaseResponse):
    """Response for governing law question."""
    response: GoverningLaw

class GoverningLawClauseNumberResponse(BaseResponse):
    """Response for governing law clause number."""
    response: str


# Eligibility Part 1 Enums and Models
class SubParticipationProvisions(BaseResponse):
    """Response for whether agreement contains express provisions relating to sub-participations."""
    response: YesNo


class SubParticipationDefined(BaseResponse):
    """Response for whether sub-participation is defined."""
    response: YesNo


class SubParticipationCaptureSRT(Enum):
    NO = "No - definition only relates to transfer of voting rights and/or total return swap or derivatives generally"
    YES = "Yes - definition expressly refers to securitisation, SRT, credit default swaps and/or any risk trade or any of the following key terms \"risk protection\", \"credit protection\", \"risk mitigation\", \"risk transfer\", \"synthetic\", \"credit default swap\", \"securitisation\", \"risk or funded\", \"funded or risk\", \"credit mitigation\", \"risk participation\""


class SubParticipationCaptureSRTResponse(BaseResponse):
    """Response for whether the definition of sub-participation captures SRT."""
    response: SubParticipationCaptureSRT


class LenderRightConditions(Enum):
    NONE = "None"
    BORROWER_CONSENT = "Borrower/Parent/Obligors consent"
    BORROWER_CONSULTATION = "Borrower/Parent/Obligors consultation"
    NOTICE_TO_BORROWER = "Notice to Borrower/Parent/Obligors"
    NOTICE_TO_AGENT = "Notice to Agent"
    PERMITTED_LENDERS = "Conditions relating to Permitted Lenders, Restricted Lenders and/or Competitors (or any similar concept)"
    OTHER = "Other"


class LenderRightConditionsResponse(BaseResponse):
    """Response for conditions applying to the Lender's right to sub-participate."""
    response: List[LenderRightConditions]


class BorrowerConsentConditions(Enum):
    NOT_UNREASONABLY_WITHHELD = "Not unreasonably withheld"
    NOT_UNREASONABLY_DELAYED = "Not unreasonably delayed"
    DEEMED_CONSENT = "Deemed consent after a certain number of days"
    NO_CONDITIONS = "No conditions apply"
    OTHER = "Other"


class BorrowerConsentConditionsResponse(BaseResponse):
    """Response for conditions applying to Borrower's/Parent's/Obligors' consent."""
    response: List[BorrowerConsentConditions]


class FormOfNoticeSpecified(BaseResponse):
    """Response for whether a form of notice is specified."""
    response: YesNo


# Eligibility Part 2 Enums and Models
class KeyTerms(Enum):
    RISK_PROTECTION = "risk protection"
    CREDIT_PROTECTION = "credit protection"
    RISK_MITIGATION = "risk mitigation" 
    RISK_TRANSFER = "risk transfer"
    SYNTHETIC = "synthetic"
    CREDIT_DEFAULT_SWAP = "credit default swap"
    SECURITISATION = "securitisation"
    RISK_OR_FUNDED = "risk or funded"
    FUNDED_OR_RISK = "funded or risk"
    CREDIT_MITIGATION = "credit mitigation"
    RISK_PARTICIPATION = "risk participation"


class KeyTermsResponse(BaseResponse):
    """Response for key terms appearing in the agreement."""
    response: List[KeyTerms]


class KeyTermsConditions(Enum):
    NONE = "None"
    BORROWER_CONSENT = "Borrower/Parent/Obligors consent"
    BORROWER_CONSULTATION = "Borrower/Parent/Obligors consultation"
    NOTICE_TO_BORROWER = "Notice to Borrower/Parent/Obligors"
    NOTICE_TO_AGENT = "Notice to Agent"
    PERMITTED_LENDERS = "Conditions relating to Permitted Lenders, Restricted Lenders and/or Competitors (or any similar concept)"
    OTHER = "Other"


class KeyTermsConditionsResponse(BaseResponse):
    """Response for conditions applying to key terms."""
    response: List[KeyTermsConditions]


# Eligibility Summary Model
class EligibilityForSRT(BaseResponse):
    """Response for whether the facility can be included in an SRT without restrictions."""
    response: YesNo


# Confidentiality and Disclosure Enums and Models
class ConfidentialityProvisions(BaseResponse):
    """Response for whether the agreement contains confidentiality/disclosure provisions."""
    response: YesNo


class DisclosurePermitted(BaseResponse):
    """Response for whether disclosure is permitted to persons entering transactions."""
    response: YesNo


class DisclosureParties(Enum):
    AFFILIATES = "Affiliates"
    PROFESSIONAL_ADVISERS = "Professional Advisers"
    REPRESENTATIVES = "Representatives"
    RELATED_FUNDS = "Related Funds"
    ALL = "All of the above"
    NONE = "None of the above"


class DisclosurePartiesResponse(BaseResponse):
    """Response for parties to whom disclosure is permitted."""
    response: List[DisclosureParties]


class NDARequiredParties(Enum):
    AFFILIATES = "Affiliates"
    PROFESSIONAL_ADVISERS = "Professional Advisers"
    REPRESENTATIVES = "Representatives"
    RELATED_FUNDS = "Related Funds"
    PERSONS_ENTERING_TRANSACTIONS = "Persons entering or potentially entering into transaction under which payments are to be made or may be made by reference to one or more Finance Documents"
    NO_NDA_REQUIRED = "No confidentiality undertaking/other form of NDA required"


class NDARequiredPartiesResponse(BaseResponse):
    """Response for parties requiring confidentiality undertaking/NDA."""
    response: List[NDARequiredParties]


class PrescribedNDAForm(BaseResponse):
    """Response for whether there is a prescribed form of confidentiality undertaking/NDA."""
    response: YesNo


class NDAFormType(Enum):
    LMA_FORM = "LMA form"
    FORM_AGREED_BY_PARTIES = "Form agreed between the parties to the Facility Agreement"
    SCHEDULE_FORM = "In the form set out in Schedule/Annex/Appendix/Side letter to loan document"
    LSTA_FORM = "LSTA form"
    OTHER_FORM = "Other form"


class NDAFormTypeResponse(BaseResponse):
    """Response for what form of confidentiality undertaking/NDA is specified."""
    response: List[NDAFormType]


class NDAFormLMABased(BaseResponse):
    """Response for whether the form is substantially in a recommended form of the LMA."""
    response: YesNo


class NDAAdditionalConditions(BaseResponse):
    """Response for whether the definition of "Confidentiality Undertaking" includes other conditions."""
    response: YesNo


class ConsentRequiredParties(Enum):
    AFFILIATES = "Affiliates"
    PROFESSIONAL_ADVISERS = "Professional Advisers"
    REPRESENTATIVES = "Representatives"
    RELATED_FUNDS = "Related Funds"
    PERSONS_ENTERING_TRANSACTIONS = "Persons entering or potentially entering into transaction under which payments are to be made or may be made by reference to one or more Finance Documents"
    NONE = "None of the above"


class ConsentRequiredPartiesResponse(BaseResponse):
    """Response for parties requiring Borrower/Obligor/Parent consent for disclosure."""
    response: List[ConsentRequiredParties]


class NotificationRequiredParties(Enum):
    AFFILIATES = "Affiliates"
    PROFESSIONAL_ADVISERS = "Professional Advisers"
    REPRESENTATIVES = "Representatives"
    RELATED_FUNDS = "Related Funds"
    PERSONS_ENTERING_TRANSACTIONS = "Persons entering or potentially entering into transaction under which payments are to be made or may be made by reference to one or more Finance Documents"
    NONE = "None of the above"


class NotificationRequiredPartiesResponse(BaseResponse):
    """Response for parties requiring notification for disclosure."""
    response: List[NotificationRequiredParties]


class NDARequirements(Enum):
    CONSENT_REQUIRED = "Requirement to obtain consent in relation to the Confidentiality undertaking/NDA"
    NOTIFICATION_REQUIRED = "Requirement to notify in relation to the Confidentiality undertaking/NDA"
    COPY_BEFORE_DISCLOSURE = "Requirement to send a copy of the Confidentiality Undertaking to the Borrower/Parent/Obligors before disclosure"
    COPY_AFTER_DISCLOSURE = "Requirement to send a copy of the confidentiality undertaking to the Borrower/Parent/Obligors after disclosure"
    NO_REQUIREMENTS = "No requirements"
    NO_NDA_REQUIRED = "No confidentiality undertaking/ other form of NDA required"


class NDARequirementsResponse(BaseResponse):
    """Response for requirements related to confidentiality undertaking/NDA."""
    response: List[NDARequirements]


class DisclosureRestrictions(Enum):
    PERMITTED_LENDERS = "Permitted Lenders"
    RESTRICTED_LENDERS = "Restricted Lenders"
    COMPETITORS = "Competitors (or any similar concept)"
    NO_RESTRICTIONS = "No restrictions"
    NO_CONCEPTS = "No Permitted Lender/Restricted Lender/Competitor concepts"


class DisclosureRestrictionsResponse(BaseResponse):
    """Response for restrictions on Lender disclosure."""
    response: List[DisclosureRestrictions]


class DisclosurePermittedWithoutConditions(BaseResponse):
    """Response for whether disclosure is permitted without conditions."""
    response: YesNo


class NatwestAffiliatesDisclosure(BaseResponse):
    """Response for whether disclosure is permitted to NatWest affiliates."""
    response: YesNo


class NatwestRepresentativesDisclosure(BaseResponse):
    """Response for whether disclosure is permitted to NatWest representatives."""
    response: YesNo


# Additional Borrowers Enums and Models
class AdditionalBorrowersProvision(BaseResponse):
    """Response for whether the agreement provides for additional borrowers."""
    response: YesNo


class LenderConsentType(Enum):
    SIMPLE_MAJORITY = "Consent of Simple majority Lenders (over 50%)"
    SIMPLE_MAJORITY_PLUS_AFFECTED = "Consent of simple majority plus consent of affected lenders"
    MAJORITY_LENDERS = "Consent of Majority Lenders (66.666%)"
    SUPER_MAJORITY = "Consent of Super majority Lenders (75%)"
    ALL_LENDERS = "Consent of all Lenders"
    SILENT = "Silent"
    ALL_AFFECTED_LENDERS = "Consent of all affected Lenders"
    MAJORITY_PLUS_AFFECTED = "Consent of Majority (66.666%) plus consent of affected Lenders"
    OTHER = "Other"
    NO_CONSENT = "No Lender consent required"


class LenderConsentTypeResponse(BaseResponse):
    """Response for what type of lender consent is required for additional borrowers."""
    response: LenderConsentType


# Interest Rate Provisions Enums and Models
class InterestRateFloor(BaseResponse):
    """Response for whether the facility contains an interest rate floor."""
    response: YesNo


class InterestRateFloorNonZero(BaseResponse):
    """Response for whether the interest rate floor is set at a rate other than zero."""
    response: YesNo


class InterestRateCap(BaseResponse):
    """Response for whether the facility contains an interest rate cap."""
    response: YesNo


# Prepayment Fee Enums and Models
class PrepaymentFeePayable(BaseResponse):
    """Response for whether a charge or fee is payable on prepayments."""
    response: YesNo


class PrepaymentAmountPermitted(BaseResponse):
    """Response for whether prepayments are permitted up to a certain amount before charges."""
    response: YesNo


class PrepaymentWithoutFeeDate(Enum):
    YES = "Yes"
    NO = "No"
    YES_UNABLE_TO_CONFIRM = "Yes but unable to confirm date"


class PrepaymentWithoutFeeDateResponse(BaseResponse):
    """Response for whether there is a date after which prepayment can be made without fee."""
    response: PrepaymentWithoutFeeDate


# Container class for full responses
class SRTChecklist(BaseModel):
    """Complete SRT checklist with all responses."""
    
    # Agreement Details
    governing_law: Optional[GoverningLawResponse] = None
    governing_law_clause_number: Optional[str] = None
    
    # Eligibility Part 1
    sub_participation_provisions: Optional[SubParticipationProvisions] = None
    sub_participation_defined: Optional[SubParticipationDefined] = None
    sub_participation_definition: Optional[str] = None
    sub_participation_captures_srt: Optional[SubParticipationCaptureSRTResponse] = None
    lender_right_conditions: Optional[LenderRightConditionsResponse] = None
    lender_right_restrictions: Optional[str] = None
    lender_right_other_conditions: Optional[str] = None
    borrower_consent_conditions: Optional[BorrowerConsentConditionsResponse] = None
    borrower_consent_other_conditions: Optional[str] = None
    deemed_consent_days: Optional[int] = None
    deemed_consent_period_type: Optional[DaysBusinessDays] = None
    notice_days: Optional[int] = None
    notice_period_type: Optional[DaysBusinessDays] = None
    form_of_notice_specified: Optional[FormOfNoticeSpecified] = None
    form_of_notice_details: Optional[str] = None
    consultation_days: Optional[int] = None
    
    # Eligibility Part 2
    key_terms_in_agreement: Optional[KeyTermsResponse] = None
    key_terms_provision: Optional[str] = None
    key_terms_conditions: Optional[KeyTermsConditionsResponse] = None
    key_terms_restrictions: Optional[str] = None
    key_terms_other_conditions: Optional[str] = None
    kt_borrower_consent_conditions: Optional[BorrowerConsentConditionsResponse] = None
    kt_borrower_consent_other_conditions: Optional[str] = None
    kt_deemed_consent_days: Optional[int] = None
    kt_deemed_consent_period_type: Optional[DaysBusinessDays] = None
    kt_notice_days: Optional[int] = None
    kt_notice_period_type: Optional[DaysBusinessDays] = None
    kt_form_of_notice_specified: Optional[FormOfNoticeSpecified] = None
    kt_form_of_notice_details: Optional[str] = None
    kt_consultation_days: Optional[int] = None
    
    # Eligibility
    eligible_for_srt: Optional[EligibilityForSRT] = None
    eligible_for_srt_details: Optional[str] = None
    
    # Confidentiality and Disclosure
    confidentiality_provisions: Optional[ConfidentialityProvisions] = None
    confidentiality_clause: Optional[str] = None
    disclosure_permitted: Optional[DisclosurePermitted] = None
    disclosure_provision: Optional[str] = None
    disclosure_permitted_parties: Optional[DisclosurePartiesResponse] = None
    nda_required_parties: Optional[NDARequiredPartiesResponse] = None
    confidentiality_undertaking_definition: Optional[str] = None
    prescribed_nda_form: Optional[PrescribedNDAForm] = None
    nda_form_type: Optional[NDAFormTypeResponse] = None
    schedule_form_lma_based: Optional[NDAFormLMABased] = None
    other_form_lma_based: Optional[NDAFormLMABased] = None
    nda_additional_conditions: Optional[NDAAdditionalConditions] = None
    nda_additional_conditions_details: Optional[str] = None
    consent_required_parties: Optional[ConsentRequiredPartiesResponse] = None
    consent_provision: Optional[str] = None
    notification_required_parties: Optional[NotificationRequiredPartiesResponse] = None
    notification_provision: Optional[str] = None
    nda_requirements: Optional[NDARequirementsResponse] = None
    nda_consent_provision: Optional[str] = None
    disclosure_restrictions: Optional[DisclosureRestrictionsResponse] = None
    disclosure_restriction_details: Optional[str] = None
    disclosure_permitted_without_conditions: Optional[DisclosurePermittedWithoutConditions] = None
    natwest_affiliates_disclosure: Optional[NatwestAffiliatesDisclosure] = None
    natwest_affiliates_restrictions: Optional[str] = None
    natwest_representatives_disclosure: Optional[NatwestRepresentativesDisclosure] = None
    natwest_representatives_restrictions: Optional[str] = None
    representatives_definition: Optional[str] = None
    
    # Additional Borrowers
    additional_borrowers_provision: Optional[AdditionalBorrowersProvision] = None
    lender_consent_type: Optional[LenderConsentTypeResponse] = None
    lender_consent_requirements: Optional[str] = None
    
    # Interest Rate Provisions
    interest_rate_floor: Optional[InterestRateFloor] = None
    interest_rate_floor_non_zero: Optional[InterestRateFloorNonZero] = None
    interest_rate_floor_rate: Optional[str] = None
    interest_rate_cap: Optional[InterestRateCap] = None
    interest_rate_cap_details: Optional[str] = None
    
    # Prepayment Fee
    prepayment_fee_payable: Optional[PrepaymentFeePayable] = None
    prepayment_amount_permitted: Optional[PrepaymentAmountPermitted] = None
    prepayment_threshold: Optional[str] = None
    prepayment_without_fee_date: Optional[PrepaymentWithoutFeeDateResponse] = None
    prepayment_without_fee_date_details: Optional[str] = None
    prepayment_fees: Optional[str] = None
    prepayment_fee_clause: Optional[str] = None