from django.db import models
from django.utils import timezone


class TestingData(models.Model):
    date = models.DateField(
        db_column="date",
        verbose_name="Date",
        blank=True,
        null=True,
        editable=False,
        auto_now_add=True,
    )
    index_price = models.DecimalField(
        db_column="index_price",
        max_digits=60,  # The maximum storage sizes vary
        verbose_name="Index price",
        decimal_places=15,
        help_text="",
    )
    credit_score_index_price = models.DecimalField(
        db_column="credit_score_index_price",
        max_digits=60,  # The maximum storage sizes vary
        verbose_name="Credit score index price",
        decimal_places=15,
        help_text="",
    )

    class Meta:
        db_table = "Index_price"
        verbose_name = "Index_price"
        verbose_name_plural = "Index_price"


class ConstituentMaster(models.Model):

    company_name = models.CharField(
        max_length=50,
        db_column="company_name",
        verbose_name="Company Name",
        help_text="Name of the company holding shares",
        default=None,
    )
    bb_ticker = models.CharField(
        max_length=50,
        db_column="bb_ticker",
        verbose_name="BB ticker",
        help_text="Unique identifier",
        default=None,
    )
    isin = models.CharField(
        max_length=50,
        db_column="isin",
        verbose_name="ISIN",
        help_text="Unique identifier",
    )
    cik = models.IntegerField(
        db_column="cik",
        verbose_name="CIK",
        help_text="Name of the company holding shares",
        blank=True,
        null=True,
    )

    gics_sector_code = models.IntegerField(
        db_column="gics_sector_code",
        blank=True,
        null=True,
        verbose_name="GICS SECTOR CODE",
        help_text="Differentiates each sector according to its code",
    )

    gics_sector_name = models.CharField(
        db_column="gics_sector_name",
        verbose_name="GICS SECTOR NAME",
        help_text="Name of the sector",
        max_length=50,
        default=None,
    )
    currency = models.CharField(
        db_column="currency",
        verbose_name="Currency",
        help_text="Type of currency",
        max_length=50,
        default=None,
    )
    region = models.CharField(
        max_length=50,
        db_column="region",
        verbose_name="Region",
        help_text="Country",
        default=None,
    )
    is_active = models.BooleanField(
        db_column="is_active",
        default=False,
        null=True,
        verbose_name="Is Active",
        help_text="This column is used for soft delete. Users can reactivate the entry via portal",
    )
    is_deleted = models.BooleanField(
        db_column="is_deleted",
        default=False,
        null=True,
        verbose_name="Is Delete",
        help_text="This column is used for hard delete. Users cannot reactivate the entry via portal",
    )

    created_date = models.DateTimeField(
        db_column="created_date",
        verbose_name="Created Date",
        help_text="Date on which the record was inserted. This is by default values and will be updated using python function save.",
        editable=False,
        null=True,
        auto_now_add=True,
    )
    updated_date = models.DateTimeField(
        db_column="update_date",
        verbose_name="Updated Date",
        help_text="Date on which the record was updated. This is by default values and will be updated using python function save.",
        blank=True,
        null=True,
        editable=False,
        auto_now_add=True,
    )

    class Meta:
        db_table = "Constituent_Master"
        verbose_name = "Constituent_Master"
        verbose_name_plural = "Constituent_Masters"

    def __str__(self):
        return self.company_name

    def save(self, *args, **kwargs):
        """ On save, update timestamps """
        if not self.id:
            self.created_date = timezone.now()
        self.updated_date = timezone.now()
        super().save(*args, **kwargs)


class ConstituentData(models.Model):

    constituent_master = models.ForeignKey(
        ConstituentMaster, on_delete=models.PROTECT, null=True
    )
    effective_date = models.DateField(
        db_column="effective_date",
        verbose_name="Effective Date",
        help_text="Date on which the record was updated. This is by default values and will be updated using python function save.",
        blank=True,
        editable=False,
        auto_now_add=True,
    )
    cik = models.IntegerField(
        db_column="cik",
        verbose_name="CIK",
        help_text="Name of the company holding shares",
        blank=True,
        null=True,
    )
    index_price = models.DecimalField(
        db_column="index_price",
        max_digits=60,  # The maximum storage sizes vary
        verbose_name="Index Price",
        decimal_places=10,
        help_text="Price relatives for a given stock of a company.",
    )
    adjusted_price = models.DecimalField(
        db_column="adjusted_price",
        max_digits=60,  # The maximum storage sizes vary
        verbose_name="adjusted Price",
        decimal_places=10,
        help_text="Price relatives for a given stock of a company.",
    )
    isin = models.CharField(
        max_length=50,
        db_column="isin",
        verbose_name="ISIN",
        help_text="Unique identifier",
    )
    bb_ticker = models.CharField(
        max_length=50,
        db_column="bb_ticker",
        verbose_name="BB ticker",
        help_text="Unique identifier",
        default=None,
    )
    shares_outstanding = models.DecimalField(
        db_column="shares_outstanding",
        max_digits=60,  # The maximum storage sizes vary
        verbose_name="Shares Outstanding",
        decimal_places=15,
        help_text="Stock currently held by all its shareholders",
    )
    market_cap = models.DecimalField(
        db_column="market_cap",
        max_digits=60,  # The maximum storage sizes vary
        verbose_name="Market Cap",
        decimal_places=5,
        help_text="Market value of a publicly traded company's outstanding shares",
    )
    index_shares = models.DecimalField(
        db_column="index_shares",
        max_digits=60,  # The maximum storage sizes vary
        verbose_name="Index Shares",
        decimal_places=10,
        help_text="Certain percentage of shares outstanding",
    )
    index_market_cap = models.DecimalField(
        db_column="index_market_cap",
        max_digits=60,  # The maximum storage sizes vary
        verbose_name="Index Market Cap",
        decimal_places=10,
        help_text="Market value of index shares",
    )
    index_weight = models.DecimalField(
        db_column="index_weight",
        max_digits=15,  # The maximum storage sizes vary
        verbose_name="Index Weight",
        decimal_places=15,
        help_text="Weightage is based on the free market capitalisation of those stocks",
    )

    is_active = models.BooleanField(
        db_column="is_active",
        default=True,
        verbose_name="Is Active",
        null=True,
        help_text="This column is used for soft delete. Users can reactivate the entry via portal",
    )
    is_deleted = models.BooleanField(
        db_column="is_deleted",
        default=False,
        null=True,
        verbose_name="Is Delete",
        help_text="This column is used for hard delete. Users cannot reactivate the entry via portal",
    )

    created_date = models.DateTimeField(
        db_column="created_date",
        verbose_name="Created Date",
        help_text="Date on which the record was inserted. This is by default values and will be updated using python function save.",
        editable=False,
        auto_now_add=True,
        null=True,
    )
    updated_date = models.DateTimeField(
        db_column="update_date",
        verbose_name="Updated Date",
        help_text="Date on which the record was updated. This is by default values and will be updated using python function save.",
        blank=True,
        editable=False,
        auto_now_add=True,
        null=True,
    )
    credit_score = models.DecimalField(
        db_column="credit_score",
        max_digits=15,
        verbose_name="Credit Score",
        decimal_places=10,
        blank=True,
        editable=False,
        null=True,
    )

    class Meta:
        db_table = "Constituent_Data"
        verbose_name = "Constituent_Data"
        verbose_name_plural = "Constituent_Data"

    def __str__(self):
        return self.effective_date

    def save(self, *args, **kwargs):
        """ On save, update timestamps """
        if not self.id:
            self.created_date = timezone.now()
        self.updated_date = timezone.now()
        super().save(*args, **kwargs)


class CreditScore(models.Model):
    constituent_master = models.ForeignKey(
        ConstituentMaster, on_delete=models.PROTECT, null=True
    )
    constituent_data = models.ForeignKey(
        ConstituentData, on_delete=models.PROTECT, null=True
    )

    is_active = models.BooleanField(
        db_column="is_active",
        default=True,
        null=True,
        verbose_name="Is Active",
        help_text="This column is used for soft delete. Users can reactivate the entry via portal",
    )
    is_deleted = models.BooleanField(
        db_column="is_deleted",
        default=False,
        null=True,
        verbose_name="Is Delete",
        help_text="This column is used for hard delete. Users cannot reactivate the entry via portal",
    )

    created_date = models.DateTimeField(
        db_column="created_date",
        verbose_name="Created Date",
        help_text="Date on which the record was inserted. This is by default values and will be updated using python function save.",
        editable=False,
        null=True,
        auto_now_add=True,
    )
    credit_score = models.DecimalField(
        db_column="credit_score",
        max_digits=15,
        verbose_name="Credit Score",
        decimal_places=10,
    )
    date = models.DateTimeField(
        db_column="date",
        verbose_name="Date",
        help_text="Date on which the credit score was updated.",
        blank=True,
        null=True,
        editable=False,
        auto_now_add=True,
    )
    updated_date = models.DateTimeField(
        db_column="update_date",
        verbose_name="Updated Date",
        help_text="Date on which the record was updated. This is by default values and will be updated using python function save.",
        blank=True,
        null=True,
        editable=False,
        auto_now_add=True,
    )

    class Meta:
        db_table = "Credit_Score"
        verbose_name = "Credit_Score"
        verbose_name_plural = "Credit_Scores"

    # def __str__(self):
    #     return self.company_name

    def save(self, *args, **kwargs):
        """ On save, update timestamps """
        if not self.id:
            self.created_date = timezone.now()
        self.updated_date = timezone.now()
        super().save(*args, **kwargs)


class CreditScoreWeight(models.Model):
    creditscore = models.ForeignKey(CreditScore, on_delete=models.PROTECT, null=True)
    constituent_master = models.ForeignKey(
        ConstituentMaster, on_delete=models.PROTECT, null=True
    )
    constituent_data = models.ForeignKey(
        ConstituentData, on_delete=models.PROTECT, null=True
    )
    effective_date = models.DateField(
        db_column="effective_date",
        verbose_name="Effective Date",
        help_text="Date on which the record was updated. This is by default values and will be updated using python function save.",
        blank=True,
        default=None,
        editable=False,
    )
    isin = models.CharField(
        max_length=50,
        db_column="isin",
        verbose_name="ISIN",
        help_text="Unique identifier",
        default=None,
    )
    is_active = models.BooleanField(
        db_column="is_active",
        default=True,
        verbose_name="Is Active",
        help_text="This column is used for soft delete. Users can reactivate the entry via portal",
    )
    is_deleted = models.BooleanField(
        db_column="is_deleted",
        default=False,
        verbose_name="Is Delete",
        help_text="This column is used for hard delete. Users cannot reactivate the entry via portal",
    )

    created_date = models.DateTimeField(
        db_column="created_date",
        verbose_name="Created Date",
        help_text="Date on which the record was inserted. This is by default values and will be updated using python function save.",
        editable=False,
        null=True,
        auto_now_add=True,
    )
    updated_date = models.DateTimeField(
        db_column="update_date",
        verbose_name="Updated Date",
        help_text="Date on which the record was updated. This is by default values and will be updated using python function save.",
        blank=True,
        null=True,
        editable=False,
        auto_now_add=True,
    )
    weight = models.DecimalField(
        db_column="credit_score_weight",
        verbose_name="Weight",
        max_digits=60,
        decimal_places=10,
        blank=True,
        null=True,
        editable=False,
    )

    class Meta:
        db_table = "Credit_Score_Weight"
        verbose_name = "Credit_Score_Weight"
        verbose_name_plural = "Credit_Score_Weights"

    # def __str__(self):
    #     return self.company_name

    def save(self, *args, **kwargs):
        """ On save, update timestamps """
        if not self.id:
            self.created_date = timezone.now()
        self.updated_date = timezone.now()
        super().save(*args, **kwargs)


class TrainingData(models.Model):

    constituent_master = models.ForeignKey(
        ConstituentMaster, on_delete=models.PROTECT, null=True
    )
    effective_date = models.DateField(
        db_column="effective_date",
        verbose_name="Effective Date",
        help_text="Date on which the record was updated. This is by default values and will be updated using python function save.",
        blank=True,
        editable=False,
        auto_now_add=True,
    )
    cik = models.IntegerField(
        db_column="cik",
        verbose_name="CIK",
        help_text="Name of the company holding shares",
        blank=True,
        null=True,
    )
    index_price = models.DecimalField(
        db_column="index_price",
        max_digits=60,  # The maximum storage sizes vary
        verbose_name="Index Price",
        decimal_places=10,
        help_text="Price relatives for a given stock of a company.",
    )
    isin = models.CharField(
        max_length=50,
        db_column="isin",
        verbose_name="ISIN",
        help_text="Unique identifier",
    )
    shares_outstanding = models.DecimalField(
        db_column="shares_outstanding",
        max_digits=60,  # The maximum storage sizes vary
        verbose_name="Shares Outstanding",
        decimal_places=15,
        help_text="Stock currently held by all its shareholders",
    )
    market_cap = models.DecimalField(
        db_column="market_cap",
        max_digits=60,  # The maximum storage sizes vary
        verbose_name="Market Cap",
        decimal_places=5,
        help_text="Market value of a publicly traded company's outstanding shares",
    )
    index_shares = models.DecimalField(
        db_column="index_shares",
        max_digits=60,  # The maximum storage sizes vary
        verbose_name="Index Shares",
        decimal_places=10,
        help_text="Certain percentage of shares outstanding",
    )
    index_market_cap = models.DecimalField(
        db_column="index_market_cap",
        max_digits=60,  # The maximum storage sizes vary
        verbose_name="Index Market Cap",
        decimal_places=10,
        help_text="Market value of index shares",
    )
    index_weight = models.DecimalField(
        db_column="index_weight",
        max_digits=15,  # The maximum storage sizes vary
        verbose_name="Index Weight",
        decimal_places=15,
        help_text="Weightage is based on the free market capitalisation of those stocks",
    )

    is_active = models.BooleanField(
        db_column="is_active",
        default=True,
        verbose_name="Is Active",
        null=True,
        help_text="This column is used for soft delete. Users can reactivate the entry via portal",
    )
    is_deleted = models.BooleanField(
        db_column="is_deleted",
        default=False,
        null=True,
        verbose_name="Is Delete",
        help_text="This column is used for hard delete. Users cannot reactivate the entry via portal",
    )

    created_date = models.DateTimeField(
        db_column="created_date",
        verbose_name="Created Date",
        help_text="Date on which the record was inserted. This is by default values and will be updated using python function save.",
        editable=False,
        auto_now_add=True,
        null=True,
    )
    updated_date = models.DateTimeField(
        db_column="update_date",
        verbose_name="Updated Date",
        help_text="Date on which the record was updated. This is by default values and will be updated using python function save.",
        blank=True,
        editable=False,
        auto_now_add=True,
        null=True,
    )
    credit_score = models.DecimalField(
        db_column="credit_score",
        max_digits=15,
        verbose_name="Credit Score",
        decimal_places=10,
        blank=True,
        editable=False,
        null=True,
    )

    class Meta:
        db_table = "Training_Data"
        verbose_name = "Training_Data"
        verbose_name_plural = "Training_Data"

    def __str__(self):
        return self.effective_date

    def save(self, *args, **kwargs):
        """ On save, update timestamps """
        if not self.id:
            self.created_date = timezone.now()
        self.updated_date = timezone.now()
        super().save(*args, **kwargs)


class AdjustedPrice(models.Model):
    constituent_master = models.ForeignKey(
        ConstituentMaster, on_delete=models.PROTECT, null=True
    )

    adjusted_price = models.DecimalField(
        db_column="adjusted_price",
        max_digits=60,  # The maximum storage sizes vary
        verbose_name="adjusted Price",
        decimal_places=10,
        help_text="Price relatives for a given stock of a company.",
        default=None,
    )
    isin = models.CharField(
        max_length=50,
        db_column="isin",
        verbose_name="ISIN",
        help_text="Unique identifier",
        default=None,
    )
    bb_ticker = models.CharField(
        max_length=50,
        db_column="bb_ticker",
        verbose_name="BB ticker",
        help_text="Unique identifier",
        default=None,
    )
    is_active = models.BooleanField(
        db_column="is_active",
        default=True,
        verbose_name="Is Active",
        null=True,
        help_text="This column is used for soft delete. Users can reactivate the entry via portal",
    )
    is_deleted = models.BooleanField(
        db_column="is_deleted",
        default=False,
        null=True,
        verbose_name="Is Delete",
        help_text="This column is used for hard delete. Users cannot reactivate the entry via portal",
    )

    created_date = models.DateTimeField(
        db_column="created_date",
        verbose_name="Created Date",
        help_text="Date on which the record was inserted. This is by default values and will be updated using python function save.",
        editable=False,
        auto_now_add=True,
        null=True,
    )
    updated_date = models.DateTimeField(
        db_column="update_date",
        verbose_name="Updated Date",
        help_text="Date on which the record was updated. This is by default values and will be updated using python function save.",
        blank=True,
        editable=False,
        auto_now_add=True,
        null=True,
    )

    effective_date = models.DateField(
        db_column="effective_date",
        verbose_name="Effective Date",
        help_text="Date on which the record was updated. This is by default values and will be updated using python function save.",
        blank=True,
        editable=False,
        default=None,
    )
    cik = models.IntegerField(
        db_column="cik",
        verbose_name="CIK",
        help_text="Name of the company holding shares",
        blank=True,
        null=True,
    )

    class Meta:
        db_table = "adjusted_price"
        verbose_name = "Adjusted_Price"
        verbose_name_plural = "Adjusted_Price"

    def __str__(self):
        return self.effective_date

    def save(self, *args, **kwargs):
        """ On save, update timestamps """
        if not self.id:
            self.created_date = timezone.now()
        self.updated_date = timezone.now()
        super().save(*args, **kwargs)


class CreditScoreWeightSquare(models.Model):
    creditscore = models.ForeignKey(CreditScore, on_delete=models.PROTECT, null=True)
    constituent_master = models.ForeignKey(
        ConstituentMaster, on_delete=models.PROTECT, null=True
    )
    constituent_data = models.ForeignKey(
        ConstituentData, on_delete=models.PROTECT, null=True
    )
    effective_date = models.DateField(
        db_column="effective_date",
        verbose_name="Effective Date",
        help_text="Date on which the record was updated. This is by default values and will be updated using python function save.",
        blank=True,
        default=None,
        editable=False,
    )
    isin = models.CharField(
        max_length=50,
        db_column="isin",
        verbose_name="ISIN",
        help_text="Unique identifier",
        default=None,
    )
    is_active = models.BooleanField(
        db_column="is_active",
        default=True,
        verbose_name="Is Active",
        help_text="This column is used for soft delete. Users can reactivate the entry via portal",
    )
    is_deleted = models.BooleanField(
        db_column="is_deleted",
        default=False,
        verbose_name="Is Delete",
        help_text="This column is used for hard delete. Users cannot reactivate the entry via portal",
    )

    created_date = models.DateTimeField(
        db_column="created_date",
        verbose_name="Created Date",
        help_text="Date on which the record was inserted. This is by default values and will be updated using python function save.",
        editable=False,
        null=True,
        auto_now_add=True,
    )
    updated_date = models.DateTimeField(
        db_column="update_date",
        verbose_name="Updated Date",
        help_text="Date on which the record was updated. This is by default values and will be updated using python function save.",
        blank=True,
        null=True,
        editable=False,
        auto_now_add=True,
    )
    weight = models.DecimalField(
        db_column="credit_score_weight",
        verbose_name="credit_score_weight",
        max_digits=60,
        decimal_places=10,
        blank=True,
        null=True,
        editable=False,
    )

    class Meta:
        db_table = "Credit_Score_Weight_Square"
        verbose_name = "Credit_Score_Weight_Square"
        verbose_name_plural = "Credit_Score_Weights_Square"
    
class CreditScoreWeightCube(models.Model):
    creditscore = models.ForeignKey(CreditScore, on_delete=models.PROTECT, null=True)
    constituent_master = models.ForeignKey(
        ConstituentMaster, on_delete=models.PROTECT, null=True
    )
    constituent_data = models.ForeignKey(
        ConstituentData, on_delete=models.PROTECT, null=True
    )
    effective_date = models.DateField(
        db_column="effective_date",
        verbose_name="Effective Date",
        help_text="Date on which the record was updated. This is by default values and will be updated using python function save.",
        blank=True,
        default=None,
        editable=False,
    )
    isin = models.CharField(
        max_length=50,
        db_column="isin",
        verbose_name="ISIN",
        help_text="Unique identifier",
        default=None,
    )
    is_active = models.BooleanField(
        db_column="is_active",
        default=True,
        verbose_name="Is Active",
        help_text="This column is used for soft delete. Users can reactivate the entry via portal",
    )
    is_deleted = models.BooleanField(
        db_column="is_deleted",
        default=False,
        verbose_name="Is Delete",
        help_text="This column is used for hard delete. Users cannot reactivate the entry via portal",
    )

    created_date = models.DateTimeField(
        db_column="created_date",
        verbose_name="Created Date",
        help_text="Date on which the record was inserted. This is by default values and will be updated using python function save.",
        editable=False,
        null=True,
        auto_now_add=True,
    )
    updated_date = models.DateTimeField(
        db_column="update_date",
        verbose_name="Updated Date",
        help_text="Date on which the record was updated. This is by default values and will be updated using python function save.",
        blank=True,
        null=True,
        editable=False,
        auto_now_add=True,
    )
    weight = models.DecimalField(
        db_column="credit_score_weight",
        verbose_name="credit_score_weight",
        max_digits=60,
        decimal_places=10,
        blank=True,
        null=True,
        editable=False,
    )

    class Meta:
        db_table = "Credit_Score_Weight_cube"
        verbose_name = "Credit_Score_Weight_cube"
        verbose_name_plural = "Credit_Score_Weights_cube"


class CreditScoreWeightQuartic(models.Model):
    creditscore = models.ForeignKey(CreditScore, on_delete=models.PROTECT, null=True)
    constituent_master = models.ForeignKey(
        ConstituentMaster, on_delete=models.PROTECT, null=True
    )
    constituent_data = models.ForeignKey(
        ConstituentData, on_delete=models.PROTECT, null=True
    )
    effective_date = models.DateField(
        db_column="effective_date",
        verbose_name="Effective Date",
        help_text="Date on which the record was updated. This is by default values and will be updated using python function save.",
        blank=True,
        default=None,
        editable=False,
    )
    isin = models.CharField(
        max_length=50,
        db_column="isin",
        verbose_name="ISIN",
        help_text="Unique identifier",
        default=None,
    )
    is_active = models.BooleanField(
        db_column="is_active",
        default=True,
        verbose_name="Is Active",
        help_text="This column is used for soft delete. Users can reactivate the entry via portal",
    )
    is_deleted = models.BooleanField(
        db_column="is_deleted",
        default=False,
        verbose_name="Is Delete",
        help_text="This column is used for hard delete. Users cannot reactivate the entry via portal",
    )

    created_date = models.DateTimeField(
        db_column="created_date",
        verbose_name="Created Date",
        help_text="Date on which the record was inserted. This is by default values and will be updated using python function save.",
        editable=False,
        null=True,
        auto_now_add=True,
    )
    updated_date = models.DateTimeField(
        db_column="update_date",
        verbose_name="Updated Date",
        help_text="Date on which the record was updated. This is by default values and will be updated using python function save.",
        blank=True,
        null=True,
        editable=False,
        auto_now_add=True,
    )
    weight = models.DecimalField(
        db_column="credit_score_weight",
        verbose_name="credit_score_weight",
        max_digits=60,
        decimal_places=10,
        blank=True,
        null=True,
        editable=False,
    )

    class Meta:
        db_table = "Credit_Score_Weight_quartic"
        verbose_name = "Credit_Score_Weight_quartic"
        verbose_name_plural = "Credit_Score_Weights_quartic"



class SquaredIndexPrice(models.Model):
    date = models.DateField(
        db_column="date",
        verbose_name="Date",
        blank=True,
        null=True,
        editable=False,
        auto_now_add=True,
    )
    index_price = models.DecimalField(
        db_column="index_price",
        max_digits=60,  # The maximum storage sizes vary
        verbose_name="Index price",
        decimal_places=15,
        help_text="",
    )
    credit_score_index_price = models.DecimalField(
        db_column="credit_score_index_price",
        max_digits=60,  # The maximum storage sizes vary
        verbose_name="Credit score index price",
        decimal_places=15,
        help_text="",
    )

    class Meta:
        db_table = "squared_index_price"
        verbose_name = "squared_index_price"
        verbose_name_plural = "squared_index_price"    



class CubedIndexPrice(models.Model):
    date = models.DateField(
        db_column="date",
        verbose_name="Date",
        blank=True,
        null=True,
        editable=False,
        auto_now_add=True,
    )
    index_price = models.DecimalField(
        db_column="index_price",
        max_digits=60,  # The maximum storage sizes vary
        verbose_name="Index price",
        decimal_places=15,
        help_text="",
    )
    credit_score_index_price = models.DecimalField(
        db_column="credit_score_index_price",
        max_digits=60,  # The maximum storage sizes vary
        verbose_name="Credit score index price",
        decimal_places=15,
        help_text="",
    )

    class Meta:
        db_table = "cubed_index_price"
        verbose_name = "cubed_index_price"
        verbose_name_plural = "cubed_index_price"    



class QuarticIndexPrice(models.Model):
    date = models.DateField(
        db_column="date",
        verbose_name="Date",
        blank=True,
        null=True,
        editable=False,
        auto_now_add=True,
    )
    index_price = models.DecimalField(
        db_column="index_price",
        max_digits=60,  # The maximum storage sizes vary
        verbose_name="Index price",
        decimal_places=15,
        help_text="",
    )
    credit_score_index_price = models.DecimalField(
        db_column="credit_score_index_price",
        max_digits=60,  # The maximum storage sizes vary
        verbose_name="Credit score index price",
        decimal_places=15,
        help_text="",
    )

    class Meta:
        db_table = "quartic_index_price"
        verbose_name = "quartic_index_price"
        verbose_name_plural = "quartic_index_price"    


class Return(models.Model):

    id= models.AutoField(
    db_column="id",
    verbose_name="Id",
    primary_key=True,
    help_text="Auto incremental unique interger values.",
    blank=True,
        )


    return_appreciation = models.CharField(
        max_length=50,
        db_column="return_appreciation",
        verbose_name="Return Appreciation",
        help_text="Time span",
        default=None,   
    )
    date = models.DateField(
        db_column="date",
        verbose_name="Date",
        blank=True,
        null=True,
        editable=False,
        auto_now_add=True,
    )
    sn500 = models.CharField(
        max_length=50,
        db_column="sn500",
        verbose_name="SN 500",
        help_text="Amount of returns achieved by SN 500 index",
        default=None,
    )
    decimalpoint_500 = models.CharField(
        db_column="decimalpoint_500",
        max_length=50,
        verbose_name="Decimal Point 500",
        help_text="Amount of returns achieved by Decimal point 500 index",
        default=None,
    )

    class Meta:
        db_table = "Returns"
        verbose_name = "Returns"
        verbose_name_plural = "Returns"

    def __str__(self):
        return self.date

    def save(self, *args, **kwargs):
        """ On save, update timestamps """
        if not self.id:
            self.created_date = timezone.now()
        self.updated_date = timezone.now()
        super().save(*args, **kwargs)


class ReturnSquare(models.Model):

    id= models.AutoField(
    db_column="id",
    verbose_name="Id",
    primary_key=True,
    help_text="Auto incremental unique interger values.",
    blank=True,
        )


    return_appreciation = models.CharField(
        max_length=50,
        db_column="return_appreciation",
        verbose_name="Return Appreciation",
        help_text="Time span",
        default=None,   
    )
    date = models.DateField(
        db_column="date",
        verbose_name="Date",
        blank=True,
        null=True,
        editable=False,
        auto_now_add=True,
    )
    sn500 = models.CharField(
        max_length=50,
        db_column="sn500",
        verbose_name="SN 500",
        help_text="Amount of returns achieved by SN 500 index",
        default=None,
    )
    decimalpoint_500 = models.CharField(
        db_column="decimalpoint_500",
        max_length=50,
        verbose_name="Decimal Point 500",
        help_text="Amount of returns achieved by Decimal point 500 index",
        default=None,
    )

    class Meta:
        db_table = "Returns_square"
        verbose_name = "Returns_square"
        verbose_name_plural = "Returns_square"

    def __str__(self):
        return self.date

    def save(self, *args, **kwargs):
        """ On save, update timestamps """
        if not self.id:
            self.created_date = timezone.now()
        self.updated_date = timezone.now()
        super().save(*args, **kwargs)



class ReturnCube(models.Model):

    id= models.AutoField(
    db_column="id",
    verbose_name="Id",
    primary_key=True,
    help_text="Auto incremental unique interger values.",
    blank=True,
        )


    return_appreciation = models.CharField(
        max_length=50,
        db_column="return_appreciation",
        verbose_name="Return Appreciation",
        help_text="Time span",
        default=None,   
    )
    date = models.DateField(
        db_column="date",
        verbose_name="Date",
        blank=True,
        null=True,
        editable=False,
        auto_now_add=True,
    )
    sn500 = models.CharField(
        max_length=50,
        db_column="sn500",
        verbose_name="SN 500",
        help_text="Amount of returns achieved by SN 500 index",
        default=None,
    )
    decimalpoint_500 = models.CharField(
        db_column="decimalpoint_500",
        max_length=50,
        verbose_name="Decimal Point 500",
        help_text="Amount of returns achieved by Decimal point 500 index",
        default=None,
    )

    class Meta:
        db_table = "Returns_cube"
        verbose_name = "Returns_cube"
        verbose_name_plural = "Returns_cube"

    def __str__(self):
        return self.date

    def save(self, *args, **kwargs):
        """ On save, update timestamps """
        if not self.id:
            self.created_date = timezone.now()
        self.updated_date = timezone.now()
        super().save(*args, **kwargs)


class CreditScoreWeightCustom(models.Model):
    creditscore = models.ForeignKey(CreditScore, on_delete=models.PROTECT, null=True)
    constituent_master = models.ForeignKey(
        ConstituentMaster, on_delete=models.PROTECT, null=True
    )
    constituent_data = models.ForeignKey(
        ConstituentData, on_delete=models.PROTECT, null=True
    )
    effective_date = models.DateField(
        db_column="effective_date",
        verbose_name="Effective Date",
        help_text="Date on which the record was updated. This is by default values and will be updated using python function save.",
        blank=True,
        default=None,
        editable=False,
    )
    isin = models.CharField(
        max_length=50,
        db_column="isin",
        verbose_name="ISIN",
        help_text="Unique identifier",
        default=None,
    )
    is_active = models.BooleanField(
        db_column="is_active",
        default=True,
        verbose_name="Is Active",
        help_text="This column is used for soft delete. Users can reactivate the entry via portal",
    )
    is_deleted = models.BooleanField(
        db_column="is_deleted",
        default=False,
        verbose_name="Is Delete",
        help_text="This column is used for hard delete. Users cannot reactivate the entry via portal",
    )

    created_date = models.DateTimeField(
        db_column="created_date",
        verbose_name="Created Date",
        help_text="Date on which the record was inserted. This is by default values and will be updated using python function save.",
        editable=False,
        null=True,
        auto_now_add=True,
    )
    updated_date = models.DateTimeField(
        db_column="update_date",
        verbose_name="Updated Date",
        help_text="Date on which the record was updated. This is by default values and will be updated using python function save.",
        blank=True,
        null=True,
        editable=False,
        auto_now_add=True,
    )
    weight = models.DecimalField(
        db_column="credit_score_weight",
        verbose_name="credit_score_weight",
        max_digits=60,
        decimal_places=10,
        blank=True,
        null=True,
        editable=False,
    )

    class Meta:
        db_table = "Credit_Score_Weight_custom"
        verbose_name = "Credit_Score_Weight_custom"
        verbose_name_plural = "Credit_Score_Weights_custom"

    def __str__(self):
        return self.id

    def save(self, *args, **kwargs):
        """ On save, update timestamps """
        if not self.id:
            self.created_date = timezone.now()
        self.updated_date = timezone.now()
        super().save(*args, **kwargs)


class CustomIndexPrice(models.Model):
    date = models.DateField(
        db_column="date",
        verbose_name="Date",
        blank=True,
        null=True,
        editable=False,
        auto_now_add=True,
    )
    index_price = models.DecimalField(
        db_column="index_price",
        max_digits=60,  # The maximum storage sizes vary
        verbose_name="Index price",
        decimal_places=15,
        help_text="",
    )
    credit_score_index_price = models.DecimalField(
        db_column="credit_score_index_price",
        max_digits=60,  # The maximum storage sizes vary
        verbose_name="Credit score index price",
        decimal_places=15,
        help_text="",
    )

    class Meta:
        db_table = "custom_index_price"
        verbose_name = "custom_index_price"
        verbose_name_plural = "custom_index_price"    

    def __str__(self):
        return self.id

    def save(self, *args, **kwargs):
        """ On save, update timestamps """
        if not self.id:
            self.created_date = timezone.now()
        self.updated_date = timezone.now()
        super().save(*args, **kwargs)